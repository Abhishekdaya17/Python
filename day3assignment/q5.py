'''Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0'''
s1,s2,s3=map(int,input("enter your marks of all three subject by spacing them:").split(" "))
print("your Average is",(s1+s2+s3)/3)