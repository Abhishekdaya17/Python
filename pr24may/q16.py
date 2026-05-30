'''16Count total occurrences of a character. S = "programming", Char = 'g' 2 '''
s = input("s = ")
ch=input("char=")
count=0
for i in range(0,len(s)):
    ch1=s[i]
    if ch1==ch:
        count=count+1

print(count)
        