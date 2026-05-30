'''42Check if two strings are equal without using equals(). S1 = "abc", S2 = "abc" TRUE 4'''
str1 = input("str1=")
str2 = input("str2=")

res = True

if len(str1) != len(str2):
    res = False
else:
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            res = False
            break

print(res)