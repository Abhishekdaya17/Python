'''106 Generate all subsequences of a string. S = "ab" "", "a", "b", "ab"'''
s=input("enter the string:")
for i in range(0,len(s)):
    for j in range(i,len(s)):
        print(s[i:j+1],end=" ")

        