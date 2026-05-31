'''3. Missing Number Detector
==========================

Scenario

Numbers from 1 to N should exist in a sequence, but one number is missing.

Requirements

* Read N and list elements from user
* Find the missing number
* Assume numbers belong to the range 1 to N+1

Test Case 1

Input:
[1, 2, 3, 5]

Output:
Missing Number = 4

Test Case 2

Input:
[2, 3, 4, 5]

Output:
Missing Number = 1

Test Case 3

Input:
[1, 2, 4, 5]

Output:
Missing Number = 3'''
'''n=int(input("input:"))
a=[]
for i in range(n):
    str=int(input("enter the number="))
    a.append(str)
if a[0]!=1:
    print("1")
else:
    for i in range(0,len(a)-1):
        if a[i]!=a[i+1]-1:
            print(a[i]+1)'''
n=int(input("input: "))
a=[]

for i in range(n):
    num=int(input("enter the number="))
    a.append(num)

for i in range(1,n+2):
    if i not in a:
        print("Missing Number =",i)
        break