'''
# 6. AI Chat Toxic Pattern Detector

An AI moderation system wants to detect whether a sentence contains three consecutive repeating characters.

If found:

```text
Spam Pattern Found
```

Else:

```text
Clean Message
```

### Input:

```text
heyyy broooo welcome
```

### Output:

```text
Spam Pattern Found'''
s=input("input: ")

for i in range(len(s)-2):
    if s[i]==s[i+1] and s[i]==s[i+2]:
        a="spam pattern found"
        break
    else:

        a="Clean Message"
print(a)