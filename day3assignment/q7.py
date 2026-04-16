'''VAssignment 7: Circle Area Calculator

Write a Python program that:

Accepts radius.
Calculates area of circle.

Input:
Radius = 7

Output:
Area = 153.86'''
import math

x=int(input("enter the radius of circle" \
"e:"))
a=math.pi*x*x

print("your area is :",round(abs(a),3))
