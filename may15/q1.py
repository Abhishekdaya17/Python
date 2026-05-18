

'''1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8
'''
n=input("input:")
count=0
i=0
while i<len(n):
    ch=n[i]
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" \
          or ch=="U":
        count=count+1
    
    i=i+1
print("output=",count)    