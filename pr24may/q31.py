'''31Remove duplicate words from a string. S = "the cat and th
e dog" "the cat and dog" 3'''

s=input("input:")

words=s.split()
result=""

newstr=""
for i in range(0,len(words)):
    ch=words[i]
    if ch not in newstr:
        newstr=newstr+ch
        
        result=result+ch+" "
        

print(result)