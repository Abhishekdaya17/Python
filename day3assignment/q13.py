'''Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0
'''

p,r,t=map(int,input("enter your pricipal rate and time").split())
aadha=(1+(r/100))**t
total=p*aadha
inter= (total-p)
print("total amount:",total)
print("your interest is",round(inter,3))