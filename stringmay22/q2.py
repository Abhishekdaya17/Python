'''# 2. AI Auto-Correct Consecutive Word Remover

An AI-powered typing assistant often captures duplicate consecutive words while converting speech into text.

The company wants a Python program that removes only consecutive duplicate words while preserving the original sentence structure.

### Input:

```text
hello hello hello team meeting meeting started
```

### Output:

```text
hello team meeting started'''
s=input("input:")
words=s.split()
unique=""
result=""
for i in range(0,len(words)):
    ch=words[i]
    if ch not in unique:
        unique=unique+ch
        result=result+ch+" "
print(result)