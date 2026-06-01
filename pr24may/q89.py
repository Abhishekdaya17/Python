'''89 Remove 'b' and 'ac' from a string. S = "abacbb" "c'''
s = input("Enter string: ")

i = 0
ans = ""

while i < len(s):

    if s[i] == 'b':
        i += 1
    elif i < len(s)-1 and s[i] == 'a' and s[i+1] == 'c':
        i += 2

    else:
        ans += s[i]
        i += 1
print(ans)