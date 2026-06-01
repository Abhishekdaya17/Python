'''104 Check if a string contains balanced brackets of all types ((), {}, []). S = "{[()]}" TRUE
1'''
s = input("Enter string: ")

stack = []
is_valid = True

for ch in s:

    if ch == '(' or ch == '{' or ch == '[':
        stack.append(ch)

    elif ch == ')' or ch == '}' or ch == ']':

        if len(stack) == 0:
            is_valid = False
            break

        i = len(stack) - 1
        top = stack[i]

        if (ch == ')' and top == '(') or \
           (ch == '}' and top == '{') or \
           (ch == ']' and top == '['):
            stack.pop()
        else:
            is_valid = False
            break

if len(stack) != 0:
    is_valid = False

if is_valid:
    print("TRUE")
else:
    print("FALSE")