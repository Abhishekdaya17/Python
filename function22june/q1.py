# 1.
# Employee Record Sorting (Lambda)


# A company stores employee details as (Name, Salary). The HR department wants to sort the employees based on salary.

# Task

# Write a Python program to sort the employee records using a lambda expression.

# Input
# employees = [("Rahul",45000),("Amit",30000),("Neha",55000),("Priya",40000)]
# Output
# [('Amit', 30000), ('Priya', 40000), ('Rahul', 45000), ('Neha', 55000)]
n=int(input("enter number of salary:"))
emp=[]
for i in range(n):
    t=()
    name=input("enter your name:")
    
    sal=int(input("enter your salary"))
    emp.append((name,sal))
print(emp)
s2=sorted(emp,key=lambda x:x[1])
print(s2)
