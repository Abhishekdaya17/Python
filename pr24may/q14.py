'''14Find the first occurrence of a character. S = "banana", Char = 'a' 1 (index) '''
s = input("s = ")
ch=input("char=")
for i in range(0,len(s)):
    ch1=s[i]
    if ch1==ch:
        print("index=",i)
        break

