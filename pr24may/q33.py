'''33Find the longest word. S = "find the longest word" "longest" 3'''
s=input("input:")

words=s.split()
maxl=0
res=""



for i in range(0,len(words)):
    ch=words[i]
    if len(ch)>maxl:
        maxl=len(ch)
        res=ch

print(res)