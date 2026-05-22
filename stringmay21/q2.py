'''2.
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india'''
s=input("input:")
words=s.split()
n=words

highest=0
result="" 
for i in range(0,len(words)):
    count=0
    ch=words[i]
    for j in range(0,len(n)):
        st=n[j]
        if ch==st:
            count=count+1
            if count>highest:
                highest=count
                result=ch
print(result)