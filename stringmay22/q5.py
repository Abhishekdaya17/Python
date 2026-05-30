'''# 5. Social Media Hashtag Trend Window

A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.

### Input:

```text
aabcbcdbca
```

### Output:

```text
dbca
```

### Explanation:

`dbca` contains all unique characters: a,b,c,d'''
s=input("input:")
unique=""
for i in range(0,len(s)):
    ch=s[i]
    if ch not in unique:
        unique=unique+ch
