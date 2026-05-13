'''1. Smart Shopping Mall Discount System
A shopping mall offers discounts based on customer type and purchase amount.
If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
Write a program to calculate the final payable amount using inline if only.'''
type=input("enetr the type:").lower()
bill=int(input("bill:"))
x=20 if type=="premium" and bill>5000 else 10 if type=="premium" and bill<5000 else 10 if type=="regular" and bill>3000 else 5 
final=(bill*(100-x))/100
print("final payment",final)
