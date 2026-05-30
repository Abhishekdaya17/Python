'''45 Check whether a string starts/ends with another string. S = "apple pie", Prefix = "apple", Suffix = "pie" Start: True, End: True
4'''
s=input("S=")
pr=input("prefix=")
su=input("suffix=")
res=False
print(s[0:len(pr)])
print(s[-(len(su))::])
if s[0:len(pr)]==pr and s[-(len(su)):]==su:
    res=True
print(res)
