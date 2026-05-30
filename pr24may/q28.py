'''28Count occurrences of a word. S = "word word other word", Word = "word" 3 2'''
s=input("input:")
count=0
words=s.split()
word=input("Word=")
for i in range(0,len(words)):
    ch=words[i]
    if word==ch:
        count=count+1
print(count)