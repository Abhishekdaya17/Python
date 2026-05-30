'''51 Extract only digits. S = "a1b2c3" "123"'''
s=input("input:")
new=""
for i in range(0,len(s)):
    ch=s[i]
    if ch>="0" and ch<="9":
        new=new+ch
    else:
        new=new+""
print(new)

