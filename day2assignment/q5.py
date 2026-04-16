'''Assignment 5: Shopping Tax Calculator
========================================

Your shopping cart total doesn’t include tax. A 12% GST is applied.

Write a Python program that:
- Accepts the cart total amount.
- Calculates 12% tax.
- Displays the tax and final total amount.

Example:
Cart = ₹2000
Tax = ₹240
Total = ₹2240'''
amt=int(input("enter the total amount:"))
tx=(12*amt)/100
ttl=amt+tx
print("cart=",amt,"\n","Tax:",tx,"\n","Total=",ttl)