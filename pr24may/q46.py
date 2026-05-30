'''46 Check if a substring appears at both the start and end. S = "abcabca", Sub="abca" TRUE'''
s=input("S=")

sub=input("substring=")
res=False
print(s[0:len(sub)])
print(s[-(len(sub))::])
if s[0:len(sub)]==s[-(len(sub)):]:
    res=True
print(res)
