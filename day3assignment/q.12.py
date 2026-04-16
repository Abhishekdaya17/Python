'''Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3'''
a=int(input('enter your amount:'))
x=a//100
y=(a%100)//50
z=(a-(x*100+y*50))//10
print("₹100 x",x,"\n","₹50 x ",y,"\n","₹10 x",z)

