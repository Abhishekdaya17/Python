'''1.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3'''

n=int(input("number of values:"))
a=[]
for i in range(n):
    # str=map(str,input("enter the marks:").split())
    str=int(input("enter the mark"))
    a.append(str)
print(a)
max=a[0]

min=a[0]
count=0
for i in range(1,n):
    if a[i]>max:
        max=a[i]
    if a[i]<min:
        min=a[i]
    if a[i]>75:
        count=count+1
print("highest=",max)
print("lowest=",min)
print("count above 75=",count)

