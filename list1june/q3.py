'''3.
A company stores employee salaries in a list. Employees earning less than ₹30,000 receive a ₹5,000 bonus.

Requirements
Read N and salaries from user
Use List Comprehension
Create Updated Salary List after bonus
Display updated salaries
Test Case

Input:

[25000, 35000, 28000, 50000]

Output:

Updated Salary List = [30000, 35000, 33000, 50000]'''
n=int(input("size of list:"))
a=[]

for i in range(n):
        s=int(input("enter the salary:"))
        a.append(s)
print(a)
b=[i if i>30000 else i+5000 for i in a ]
print("updated salary=",b)
