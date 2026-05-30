
'''5.
Given an unsorted array arr[] of size N having both negative and positive integers. 
The task is place all negative element at the end of array without changing the order of positive element and negative element.

Example 1:
Input : 
N = 8
arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
Output : 
1  3  2  11  6  -1  -7  -5

Example 2:
Input : 
N=8
arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}
Output :
7  9  10  11  -5  -3  -4  -1'''
n=int(input("size of list:"))
a=[]
for i in range(n):
    str=int(input("enter values:"))
    a.append(str)
print(a)
pos=[]
neg=[]
for i in range(n):
    if a[i]>=0:
        pos.append(a[i])
    else:
        neg.append(a[i])
result=pos+neg
print("output=",result)


