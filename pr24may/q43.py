'''43 Check if two strings are rotations of each other. S1 = "abcde", S2 = "cdeab" TRUE
4'''
s1=input("s1=")
s2=input("s2=")
res=False
if sorted(s1)==sorted(s2):
    res=True
print(res)