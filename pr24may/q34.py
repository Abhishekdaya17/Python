'''34Find the shortest word. S = "find the shortest word" "the" 3'''
s=input("input:")

words=s.split()
maxl=len(s)
res=""



for i in range(0,len(words)):
    ch=words[i]
    if len(ch)<maxl:
        maxl=len(ch)
        res=ch

print(res)