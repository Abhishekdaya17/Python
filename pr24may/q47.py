'''47 Check for substring using concatenation trick. S1="CDAB", S2="ABCD" True (S1 is in S2+S2)'''
s1=input("S1=")
s2=input("S2=")
conc=s1+s2
res=False
if s1 in conc:
    res=True
print(res)