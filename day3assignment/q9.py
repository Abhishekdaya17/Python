'''Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100s

Output:
Cost = 500
'''
dst,mil,pp=map(int,input("enter the distance , millage of vehical and petrol price:").split())
print("your cost is:",(dst/mil)*pp)