'''2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:

```
Python is powerful
```

Output:

```
lufrewop si nohtyP'''
n=input("input ")
rev=""
words=n.split()
n=""
i=len(words)-1
while i>=0:
    word=words[i]
    rev=word[-1::-1]
    rev1="".join(rev)
    
    n=n+rev1+" "
    i=i-1
print()    
print(n)