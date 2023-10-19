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


# Recursively find parameterized tests in the repo
def find_parameterized_tests(directory,
                             package_name="",
                             parameterized_parents=None):
    if parameterized_parents is None:
        parameterized_parents = []

    tests = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            parameterized_parents_copy = parameterized_parents.copy()
            for it in os.listdir(item_path):
                if it.endswith(".java"):
                    with open(os.path.join(item_path, it),
                              "r", encoding="utf-8") as file:
                        if has_parameterized_annotation(file.read()):
                            parameterized_parents_copy.append(it)
            tests.extend(find_parameterized_tests(item_path,
                                                  package_name + item + ".",
                                                  parameterized_parents_copy))
        elif item.endswith(".java"):
            with open(item_path, "r", encoding="utf-8") as file:
                content = file.read()
                parent_match = re.compile(parent_pattern).search(content)
                parent_class = parent_match.group(1) if parent_match else None
            if (has_parameterized_annotation(content) or
               (parent_class and parent_class in parameterized_parents)):
                package_val = re.compile(package_pattern).search(content).group(1)
                matches = re.finditer(put_pattern, content)
                for match in matches:
                    method_name = match.group(1)
                    tests.append(f"{package_val}.{item[:-5]}.{method_name}")
    return tests


# Find puts in the repo
parameterized_tests = find_parameterized_tests(repo_path)

# Report results
csv_filename = f"{repo_name}_parameterized_tests.csv"
with open(csv_filename, "w", newline="") as csvfile:
    fieldnames = ["Project URL", "Module Path", "Fully-Qualified Test Name"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for test in parameterized_tests:
        writer.writerow({
            "Project URL": repo_url,
            "Module Path": repo_name,
            "Fully-Qualified Test Name": test
        })

print(f"Parameterized tests have been saved to {csv_filename}")
