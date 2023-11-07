import csv
import os
import re

# GitHub repository URL
repo_url = "https://github.com/apache/hadoop"

# Regexes to match patterns in Java files
put_pattern = r'@(?:Test|ParameterizedTest)\s*(?:\([^)]*\)\s*)*' \
              r'(?:@\w+\s*(?:\([^)]*\)\s*)*)*public\s+\w+\s+(\w+)\s*\([^)]*\)'
package_pattern = r'package\s+([a-zA-Z_][a-zA-Z0-9_.]*);'
parent_pattern = r'extends\s+(\w+)'

# Clone the repo if it doesn't exist
# Or if the repo is in another folder, put the path into repo_path and skip the cloning part
repo_name = "hadoop"
repo_path = os.path.join(os.getcwd(), repo_name)

if not os.path.exists(repo_path):
    os.system(f'git clone {repo_url} {repo_path}')


# Check if a Java file contains a put annotation
def has_parameterized_annotation(content):
    return any(annotation in content
               for annotation in ["@RunWith(Parameterized.class)",
                                  "@ParameterizedTest",
                                  "@RunWith(value = Parameterized.class)"])

def get_module_path(file_path):
    # Get the relative path of the file from the repository root
    relative_path = os.path.relpath(file_path, repo_path)
    module_path = os.path.dirname(relative_path)
    parts = module_path.split("src")
    if len(parts) > 1:
        module_path = parts[0].rstrip(os.path.sep)
        return module_path
    return None

# ... (existing code remains the same)

# Recursively find parameterized tests in the repo
def find_parameterized_tests(directory, package_name="", parameterized_parents=None):
    if parameterized_parents is None:
        parameterized_parents = []

    tests = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            parameterized_parents_copy = parameterized_parents.copy()
            for it in os.listdir(item_path):
                if it.endswith(".java"):
                    file_path = os.path.join(item_path, it)
                    with open(file_path, "r", encoding="utf-8") as file:
                        if has_parameterized_annotation(file.read()):
                            parameterized_parents_copy.append(it)
            tests.extend(find_parameterized_tests(item_path, package_name + item + ".", parameterized_parents_copy))
        elif item.endswith(".java"):
            file_path = os.path.join(directory, item)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                parent_match = re.compile(parent_pattern).search(content)
                parent_class = parent_match.group(1) if parent_match else None

                if (has_parameterized_annotation(content) or
                   (parent_class and parent_class in parameterized_parents)):
                    package_val = re.compile(package_pattern).search(content).group(1)
                    module_path = get_module_path(file_path)
                    matches = re.finditer(put_pattern, content)
                    for match in matches:
                        method_name = match.group(1)
                        tests.append(f"{module_path.replace(os.path.sep, '/')},{package_val}.{item[:-5]}#{method_name}")
    return tests

# Find puts in the repo
parameterized_tests = find_parameterized_tests(repo_path)

csv_filename = f"{repo_name}_parameterized_tests.csv"
with open(csv_filename, "w", newline="") as csvfile:
    fieldnames = ["Project URL", "Module Path", "Fully-Qualified Test Name"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for test in parameterized_tests:
        module_path, test_name = test.split(",", 1)
        writer.writerow({
            "Project URL": repo_url,
            "Module Path": module_path,
            "Fully-Qualified Test Name": test_name
        })

print(f"Parameterized tests have been saved to {csv_filename}")
