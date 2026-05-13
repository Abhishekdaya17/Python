'''.Digit Gap Analyzer

A system analyzes the gap between consecutive digits.

Write a program to:

Traverse digits from left to right
Find the absolute difference between current digit and next digit
Display each difference
Count how many differences are greater than 2
Find the maximum difference
If all differences ≤ 2 → print Smooth Number
Else → print Irregular Pattern

Input:
86421

Output:
Differences: 2 2 2 1
Count (>2) = 0
Max Difference = 2
Smooth Number
'''
num=input("input")
prv=None
count=0
max=0

for i in num:
    
    if prv==None:
        prv=int(i)
    else:
        dif=abs(prv-int(i))
        print("difference",dif,end="")
        if dif>2:
            count=count+1

        if max<=dif:
         max=dif
        prv=int(i)
print("count=",count)
print("max",max)
if count==0:
    print("smooth number")
else:
    print("not smooth ")