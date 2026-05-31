'''====================================================================
6. Product Except Self
======================

Scenario

For every element, calculate the product of all other elements except itself.

Requirements

* Read N and list elements from user
* Create a new list containing products
* Display the result

Test Case 1

Input:
[1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Test Case 2

Input:
[2, 3, 5]

Output:
[15, 10, 6]

---'''
n=int(input("input:"))
a=[]
for i in range(n):
    str=int(input("enter the number="))
    a.append(str)

newarr=[]
for i in range(0,len(a)):
    prod=1
    
    for j in range(len(a)):
        if i!=j:
            prod=prod*a[j]
    newarr.append(prod)

print(newarr)



