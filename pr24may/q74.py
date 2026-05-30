''' 74Find the longest substring without repeating characters. S = "abcabcbb" "abc"'''
'''74 Find the longest substring without repeating characters'''

s=input("input:")
long=""
for i in range(0,len(s)):
    str1=""
    for j in range(i,len(s)):
        ch=s[j]
        if ch not in str1:
            str1=str1+ch
        else:
            break
        if len(str1)>len(long):
            long=str1
print(long)
