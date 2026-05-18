'''2.
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5'''
n=input("input:")
count=0
i=0
while i<len(n):
    ch=n[i]
    if ch==" ":
        count=count+1
    
    i=i+1
print("output=",count)  