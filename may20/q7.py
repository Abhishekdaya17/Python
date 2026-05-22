'''. Remove Duplicate Words from a String

Voice Assistant Noise Correction System

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple times.

The company wants a Python program that removes duplicate words while maintaining the original order.

``
hello hello how are are you
```

Output:

```
hello how are you
'''
s=input("input:")
words=s.split()
unique=""
result=""
i=0
while i<len(words):
    word=words[i]
    if word!=unique:
        unique=unique+word
        result+=word+" "
    i=i+1
print("Result: ",result)

