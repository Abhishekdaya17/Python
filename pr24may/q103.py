'''103 Check if a string contains balanced parentheses. S = "((()))" TRUE
'''
s = input("Enter string: ")

balance = 0
is_valid = True

for i in s:
    if i == '(':
        balance = balance + 1
    elif i == ')':
        balance = balance - 1


    if balance < 0:
        is_valid = False
        break

# final check
if balance != 0:
    is_valid = False

if is_valid:
    print("TRUE")
else:
    print("FALSE")