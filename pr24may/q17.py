'''17Remove occurrences of a character. S = "banana", Char = 'a', Remove All "bnn" 1'''
s = input("s = ")
ch=input("char=")
new=""
for i in range(0,len(s)):
    ch1=s[i]
    if ch1!=ch:
        new=new+ch1

print(new)