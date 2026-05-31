'''====================================================================
5. Equilibrium Index Finder
===========================

Scenario

Find an index where:

# Sum of elements on the left side

Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message

Test Case 1

Input:
[1, 3, 5, 2, 2]

Output:
Equilibrium Index = 2

Explanation:
1 + 3 = 2 + 2

Test Case 2

Input:
[1, 2, 3]

Output:
No Equilibrium Index Found'''
n=int(input("input:"))
a=[]
for i in range(n):
    str=int(input("enter the number="))
    a.append(str)
found=False
for i in range(0,len(a)):
    firstsum=0
    secondsum=0
    for j in range(0,i):
        firstsum=firstsum+a[j]
    for k in range(i+1,len(a)):
        secondsum=secondsum+a[k]
    if firstsum==secondsum:
        found=True
        print("index value=",i)
        break
if found==False:
    print("not found")
