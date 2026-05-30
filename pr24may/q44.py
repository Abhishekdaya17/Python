'''44 Check if two strings are anagrams. S1 = "listen", S2 = "silent" TRUE
45'''
s1=input("s1=")
s2=input("s2=")
res=False
if sorted(s1)==sorted(s2):
    res=True
print(res)