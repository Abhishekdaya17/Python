'''24Check if all characters in a string are unique. S1 = "abc", S2 = "abca" S1: True, S2: False 2'''
s=input("input:")
unique=""
for i in range(0,len(s)):
    ch=s[i]
    if ch not in unique:
        a="True"
        unique=unique+ch
    else:
        a="False"
print(a)