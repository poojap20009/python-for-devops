import re

text = "Krishna is Black"
pattern = r"Black"
replace = "Blue"

new_text = re.sub(pattern, replace, text)
print("Modified text is: ", new_text)