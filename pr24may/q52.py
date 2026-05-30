'''52 Remove all special characters. S = "a!@b#c" "abc"
5'''
s=input("input:")
new=""
for i in range(0,len(s)):
    ch=s[i]
    if ch>="a" and ch<="z" or ch>="A" and ch<="Z" or ch>="0" and ch<="9":
    
        
            new=new+ch
        
    else:
        new=new+""
print(new)
