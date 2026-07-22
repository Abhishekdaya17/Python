# 1. Count Pairs with Difference K

# A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

# Problem Statement:

# Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

# Example:

# Input:

# N = 5
# K = 2
# ages[] = {1, 5, 3, 4, 2}

# Output:

# 3

# Explanation:

# (1,3), (3,5), (2,4)
n=int(input("size of array:"))
k=int(input("enter the value of K:"))
a=[]
for i in range(0,n):
    valu=int(input("Enter the value"+str(i+1)+":"))
    a.append(valu)
print(a)
count=0

for i in range(n):
    for j in range(i,n):
        if i!=j:
            if abs(a[i]-a[j])==k:
                count=count+1
print('count=',count)

