# Regular Expression methods
import re


text = "The quick brown fox"

pattern = r"quick"
# pattern = r"The quick brown fox" # Uncomment to see match regex pattern as Matched


# Search pattern in a string
search = re.search(pattern, text)

if search:
    print("Pattern found: ", search.group())
else:
    print("Pattern not found")
    

# Pattern match in a string
match = re.match(pattern, text)

if match:
    print("Pattern matched: ", match.group())
else:
    print("Pattern not matched")


# Replace regex
text1 = "The quick brown fox jumps over the lazy brown dog"
pattern1 = r"brown"

replacement = "red"

new_text = re.sub(pattern1, replacement, text)
print("Modified text: ", new_text)


# Split regex
fruits = "apple,banana,oranges,grapes"
pattern2 = r","

split_result = re.split(pattern2, fruits)
print("Splitted text: ", split_result)

