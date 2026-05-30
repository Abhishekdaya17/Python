'''1. Smart Log File Error Pattern Detector

A cybersecurity company stores server logs containing repeated system activity characters.

To detect suspicious looping behavior, the analytics team wants a Python program that finds the longest repeating substring present in the log file.

If multiple substrings have the same length, print the first one found.

 Input:

```text
abcabcbb
```

Output:

```text
abc
```'''
s=input("input:")
uni=""
for i in range(len(s)):
    ch=s[i]
    if ch not in uni:
        uni=uni+ch

        maximum=len(uni)
for j in range(i,maximum+1):
    


    




    
    

