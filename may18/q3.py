'''3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5
'''
n=input("input:")
sp=1
l=len(n)
for i in range(0,l,1):
    ch=n[i]
    if ch==" ":
        sp=sp+1
    else:
        sp=sp+0
print("total words=",sp)