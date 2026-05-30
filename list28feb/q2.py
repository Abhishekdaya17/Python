'''2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []'''

n=int(input("number of values:"))
a=[]
for i in range(n):
    str=int(input("enter the salary:"))
    a.append(str)
print(a)
sum=0
for i in a:
    sum=sum+i
print("average=",round(sum/n,3))
count=0
for i in a:
    if i>(sum/n):
    
        print("above avergae=",i)
for i in a[:]:
    if i<15000:
    
        a.remove(i)
print(a)





