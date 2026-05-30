'''50 Remove all digits. S = "a1b2c3" "abc"'''
s=input("input:")
new=""
for i in range(0,len(s)):
    ch=s[i]
    if ch>="0" and ch<="9":
        new=new+""
    else:
        new=new+ch
print(new)
