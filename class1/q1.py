# Question 1: Employee Salary Management System
# Scenario

# A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

# Requirements

# Create a class named Employee with the following attributes:

# employee_id
# employee_name
# basic_salary

# Initialize the values using a constructor.

# Calculations
# HRA = 20% of Basic Salary
# DA = 15% of Basic Salary
# Gross Salary = Basic Salary + HRA + DA
# Sample Input
# Enter Employee ID : E101
# Enter Employee Name : Rahul Sharma
# Enter Basic Salary : 50000
# Sample Output
# ------ Employee Salary Details ------
# Employee ID      : E101
# Employee Name    : Rahul Sharma
# Basic Salary     : 50000.0
# HRA              : 10000.0
# DA               : 7500.0
# Gross Salary     : 67500.0
class Employee:
    def __init__(self,Employee_id,E_name,salary):
        self.hra=(20*salary)/100
        self.da=(15*salary)/100
        self.E_id=Employee_id
        self.E_name=E_name
        self.G_salary=salary+self.hra+self.da
        self.salary=salary


E_name=input("Enter Employee name:")
Employee_id=input("Enter employee id:")
salary=int(input("enter your salary:"))

ob=Employee(E_name,Employee_id,salary)
print(f''' ------ Employee Salary Details ------
Employee ID      : {ob.E_id}
Employee Name    : {ob.E_name}
Basic Salary     : {ob.salary}
 HRA              : {ob.hra}
 DA               : {ob.da}
 Gross Salary     : {ob.G_salary}''')
