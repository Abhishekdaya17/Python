'''65Count palindromic substrings. S = "aaa" 6 (a, a, a, aa, aa, aaa) 6'''
s=input("input:")
for i in range(0,len(s)):
    for j in range(0,len(s)):
        subs=s[i:j+1]
        if subs==subs[::-1]:
            print(subs,end=" ")