import re

text = "apple, banana, orange, grapes"
pattern = r","
new_text = re.split(pattern, text)
print("Split result: ", new_text)