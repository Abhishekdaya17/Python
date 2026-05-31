'''10. Find Duplicate Numbers
==========================

Scenario

A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

Requirements

* Read N and list elements from user
* Find all duplicate numbers
* Store duplicates in another list
* Count total duplicate numbers
* Display duplicates in sorted order

Test Case 1

Input:
[1, 2, 3, 2, 4, 5, 1]

Output:
Duplicate Numbers = [1, 2]
Count = 2

Test Case 2

Input:
[10, 20, 30]

Output:
No Duplicate Numbers Found

---'''
n=int(input("input:"))
a=[]
for i in range(n):
    str=int(input("enter the number="))
    a.append(str)

new=[]
for i in a:
    count=0
    for j in a:
        if i==j:
            count=count+1
    if count>1:
        if i not in new:
            new.append(i)
new.sort()
if len(new)==0:
    print("no duplicates")
else:
    print(new)
    print("count=",len(new))


    

