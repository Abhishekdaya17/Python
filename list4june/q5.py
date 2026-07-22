'''5.

Rearrange the array in alternating positive and negative items
Given an unsorted array Arr of N positive and negative numbers. 
Your task is to create an array of alternate positive and negative numbers 
without changing the relative order of positive and negative numbers.
Note: Array should start with positive number.

Example 1:
Input: 
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2
Example 2:
Input: 
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output:
5 -5 2 -2 4 -8 7 1 8 0'''
n=int(input("size of array:"))

a=[]
for i in range(0,n):
    valu=int(input("Enter the value"+str(i+1)+":"))
    a.append(valu)
print(a)
poslist=[]
neglist=[]
for i in a:
    if i>=0:
        poslist.append(i)
    else:
        neglist.append(i)

if len(poslist)<len(neglist):
    result=[]
    for i in range(len(neglist)):
        if i<=len(poslist)-1:
            result.append(poslist[i])
            result.append(neglist[i])
        else:
            result.append((neglist[i]))
elif len(neglist)<len(poslist):
    result=[]
    for i in range(len(poslist)):
        if i<=len(neglist)-1:
            result.append(poslist[i])
            result.append(neglist[i])
        else:
            result.append(poslist[i])
else:
    result=[]
    for i in range(len(poslist)):
        result.append(poslist[i])
        result.append(neglist[i])
print(result)
