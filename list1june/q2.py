'''2.
Student Pass List Generator (Using List Comprehension)

A school stores student marks in a list. Generate a new list containing only the marks of students who have passed (marks ≥ 40).

Requirements
Read N and marks from user
Use List Comprehension
Create Pass List
Display Pass Count
Test Case

Input:

[25, 40, 55, 78, 30, 90]

Output:

Pass List = [40, 55, 78, 90]
Pass Count = 4'''
n=int(input("size of list:"))
a=[]

for i in range(n):
        s=int(input("enter the element:"))
        a.append(s)
print(a)
b=[i for i in a if int(i)>=40]
print("pass list=",b)
print("pass count=",len(b))