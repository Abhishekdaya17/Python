'''4.Electricity Billing System
An electricity board calculates bills based on units consumed:
Up to 100 units → ₹5 per unit
101–300 units → ₹7 per unit
Above 300 units → ₹10 per unit
Write a program to compute total bill using inline if.'''
unit=int(input("unit:"))
x=5*unit if unit<=100 else 500+(unit-100)*7 if unit<=300 else (1200+(unit-300)*10)
print("your bill is",x)