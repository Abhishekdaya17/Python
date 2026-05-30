'''6.

A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0'''
n=int(input("size of list:"))
a=[]
for i in range(n):
    str=int(input("enter values:"))
    a.append(str)
print(a)
pr=[]
sum=0
count1=0
for i in range(n):
    count=0
    for j in range(1,a[i]+1):
        if a[i]%j==0:
            count=count+1
    if count==2:
        pr.append(a[i])
        sum=sum+a[i]
        count1=count1+1
max=0
for i in pr:
    if i>max:
        max=i
print("Prime IDs =",pr)
print("Sum = ",sum)

print("Max =",max)
print("Count =",count1)


