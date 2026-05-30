'''29Remove occurrences of a word. S = "a test b test c", Word = "test", Remove All "a b c" 3'''
s=input("input:")
count=0
words=s.split()
word=input("Word=")
new=""
for i in range(0,len(words)):
    ch=words[i]
    if word!=ch:
        new=new+ch+" "
print(new)