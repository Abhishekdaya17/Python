'''30Replace a word with another word. S = "old data", Old="old", New="new" "new data" 3'''
s=input("input:")
count=0
words=s.split()
word=input("Word=")
new=input("New=")
newstr=""
for i in range(0,len(words)):
    ch=words[i]
    if word==ch:
        newstr=newstr+new+" "
    else:
        newstr=newstr+ch+" "
print(newstr)