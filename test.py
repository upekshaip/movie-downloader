import re

text_with_ansi = "\x1b[0;94m 0.4%\x1b[0m"

# Define a regular expression to match the percentage
percentage_pattern = re.compile(r'(\d+(\.\d+)?)%')

# Search for the percentage in the text
match = percentage_pattern.search(text_with_ansi)

# Check if a match is found
if match:
    # Extract the matched percentage
    percentage = match.group(1)
    print(f"Extracted Percentage: {float(percentage)}")
else:
    print("No percentage found in the text.")