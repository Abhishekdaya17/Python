'''15Find the last occurrence of a character. S = "banana", Char = 'a' 5 (index) '''
s = input("s = ")
ch=input("char=")
for i in range(-1,-len(s),-1):
    ch1=s[i]
    if ch1==ch:
        print("index=",len(s)+i)
        break