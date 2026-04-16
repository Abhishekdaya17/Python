'''Assignment 6: Smart Coin Machine
========================================

You insert an amount into a vending machine. It returns coins using the largest denominations possible (₹10 and ₹5).

Write a Python program that:
- Accepts the total amount.
- Calculates how many ₹10 coins and ₹5 coins will be dispensed.
- Displays the result.

Example:
Amount = ₹35
Output = ₹10 x 3, ₹5 x 1'''
import math
amt=int(input("Enter the amount="))
tcoin=amt//10
ten=math.floor(tcoin)
fcoin=math.floor((amt%10)//5)
print("₹10 X",ten,"₹5 X",fcoin)
