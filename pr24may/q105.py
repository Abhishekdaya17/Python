'''105 Find the longest valid parentheses substring. S = "()(())" 6
'''
s = input("Enter string: ")

max_len = 0

for i in range(len(s)):

    balance = 0

    for j in range(i, len(s)):

        if s[j] == '(':
            balance = balance + 1
        elif s[j] == ')':
            balance = balance - 1

        
        if balance < 0:
            break

        
        if balance == 0:
            length = j - i + 1
            if length > max_len:
                max_len = length

print(max_len)