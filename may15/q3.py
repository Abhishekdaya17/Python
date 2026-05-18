'''Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times'''
n=input("input:")
m=input("enter the character to check ")
count=0
i=0
while i<len(n):
    ch=n[i]
    if m in ch:
        count=count+1
    
    i=i+1
print("output=",count)  