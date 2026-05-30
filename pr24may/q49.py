'''49 Replace all consonants with '*' (Example suggests replacing non-vowels). S = "apple" "ap*le" (or similar output depending on implementation)'''
s=input("input:")
new=""
for i in range(0,len(s)):
    ch=s[i]
    if ch>="a" and ch<="z" or ch>="A" and ch<="Z":
    
        if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
            new=new+ch
        else:
            new=new+"*"
    else:
        new=new+ch
print(new)