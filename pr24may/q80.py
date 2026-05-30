'''80 Print list items containing all characters of a given word.
List = ["apple", "plea"]
Word = "pal"

Output:
apple
plea
'''

s=[]

n=int(input("how many words:"))

for i in range(0,n):
    x=input("input:")
    s.append(x)

word=input("word:")

for i in range(0,len(s)):
    ch=s[i]

    ok=True

    for j in range(0,len(word)):
        if word[j] not in ch:
            ok=False

    if ok==True:
        print(ch)