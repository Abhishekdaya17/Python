'''3. Employee Bonus Distribution System
A company provides bonuses based on years of experience.
Experience >10 years → 30% bonus
Experience >5 years → 20% bonus
Otherwise → 10% bonus
Write a program to calculate the total salary after adding bonus using inline if.
'''
exp=int(input("experience:"))
sal=int(input("salary:"))
x=30 if exp>10 else 20 if exp>5 else 10
print("total salary after",((100+x)*sal)/100)