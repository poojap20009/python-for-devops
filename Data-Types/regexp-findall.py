import re

text = "Krishna is a handsome guy in the world." 
pattern = r"Krishna"

search = re.search(pattern, text)
if search:
    print("Pattern found: ", search.group())
else:
    print("Pattern not found")
