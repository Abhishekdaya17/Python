'''Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0'''
cp,sp=map(int,input("enter cost price and selling price:").split())
p=sp-cp
print("your profit/loss  is:",p,"and profit percentage :",(p*100)/cp,"%")