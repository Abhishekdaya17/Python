'''48 Remove all vowels. S = "aeiou XYZ" " XYZ"'''
s=input("input:")
new=""
for i in range(0,len(s)):
    ch=s[i]
    if ch!="a" and ch!="e" and ch!="i" and ch!="o" and ch!="u":
        new=new+ch
print(new)