'''57Merge two strings alternatively (char by char). S1 = "ABC", S2 = "def" "AdBeCf"'''
s1=input("s1=")
s2=input("s2=")
new=""
n=len(s1)
if len(s2)<n:
    n=len(s1)
for i in range(0,n):
    ch=s1[i]
    new=new+ch
    ch1=s2[i]
    new=new+ch1
print(new)



