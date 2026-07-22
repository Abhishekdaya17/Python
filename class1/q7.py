import re
text="python is easy"
res=re.match(r"is",text)
print(res.group())