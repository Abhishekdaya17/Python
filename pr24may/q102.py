'''102 Reverse a string using recursion. S = "abc" "cba"
'''
s =input("enter the string:")

result = ""

for i in s:
    result = i + result

print(result)