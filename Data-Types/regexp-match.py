import re

text = "Krishna is a handsome guy in the world." 
pattern = r"Krishna"

match = re.match(pattern, text)
if match:
    print("match found: ", match.group())
else:
    print("match not found")
