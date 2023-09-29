import csv
import re
from github import Github

# GitHub repo URL and access token
repo_url = "https://github.com/apache/hadoop"
token = ""  # Replace with a personal token

# Regexes to match patterns in Java files
put_pattern = r'@(?:Test|ParameterizedTest)\s*(?:\([^)]*\)\s*)*' \
              r'(?:@\w+\s*(?:\([^)]*\)\s*)*)*public\s+\w+\s+(\w+)\s*\([^)]*\)'
package_pattern = r'package\s+([a-zA-Z_][a-zA-Z0-9_.]*);'
parent_pattern = r'extends\s+(\w+)'

g = Github(token)
# Get the repository
repo_name = "apache/hadoop"
repo = g.get_repo(repo_name)


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
    for item in directory:
        if item.type == "dir":
            parameterized_parents_copy = parameterized_parents.copy()
            for it in repo.get_contents(item.path):
                if it.name.endswith(".java"):
                    content = it.decoded_content.decode("utf-8")
                    if has_parameterized_annotation(content):
                        print(it.name)
                        parameterized_parents_copy.append(it.name[:-5])
            tests.extend(find_parameterized_tests(repo.get_contents(item.path),
                                                  package_name + item.name + ".",
                                                  parameterized_parents_copy))
        elif item.type == "file" and item.name.endswith(".java"):
            content = item.decoded_content.decode("utf-8")
            parent_match = re.compile(parent_pattern).search(content)
            parent_class = parent_match.group(1) if parent_match else None
            if (has_parameterized_annotation(content) or
               (parent_class and parent_class in parameterized_parents)):
                package_val = re.compile(package_pattern).search(content).group(1)
                matches = re.finditer(put_pattern, content)
                for match in matches:
                    method_name = match.group(1)
                    tests.append(f"{package_val}.{item.name[:-5]}.{method_name}")
    return tests


# Find puts in the repo
parameterized_tests = find_parameterized_tests(repo.get_contents(""))

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
