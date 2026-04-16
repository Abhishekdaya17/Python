'''Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900'''
a=int(input('enter your total amount :'))
print("your total amount after 10% discount:",a-(10*a)/100)