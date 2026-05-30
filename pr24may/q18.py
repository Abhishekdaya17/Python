'''18Replace occurrences of a character. S = "apple", Old='p', New='x' "axxle" '''
s = input("s = ")
ch=input("old=")
x=input("new=")
new=""
for i in range(0,len(s)):
    ch1=s[i]
    if ch1==ch:
        new=new+x
    else:
        new=new+ch1

print(new)