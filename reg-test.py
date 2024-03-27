import re

# Corrected regex with proper syntax for named capture groups
corrected_regex = r"datasource=(?<datasource>.*?) depName=(?<depName>.*?) versioning=(?<versioning>.*?)\\n.*?=\"(?<currentValue>.*)\""
# Provided sample text
text = """
# renovate: datasource=github-releases depName=oxsecurity/megalinter-terraform versioning=loose
def megalinter_version="v7.8.0"
"""

# Attempt to match the corrected regex with the sample text
corrected_match = re.search(corrected_regex, text, re.DOTALL)

# Check if there's a match and print the result
if corrected_match:
    print("Match found!")
    print(f"Datasource: {corrected_match.group('datasource')}")
    print(f"DepName: {corrected_match.group('depName')}")
    print(f"Versioning: {corrected_match.group('versioning')}")
    print(f"CurrentValue: {corrected_match.group('currentValue')}")
else:
    print("No match found.")
