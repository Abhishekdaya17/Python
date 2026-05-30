'''# 3. Secure Banking Transaction Analyzer

A banking server generates encrypted transaction IDs using letters and digits.

The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

If no unique digit exists, print:

```text
No unique digit found
```

### Input:

```text
A122334455667789
```

### Output:

```text
8
```'''
s=input("input:")
ch=s[0]
count=0
min=len(s)
for i in range(1,len(s)):
    count=0
    ch1=s[i]
    if ch==ch1:
        count=count+1
    else:
        count=count+1
    
    