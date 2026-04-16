'''Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%'''
ttl=int(input("enter total marks:"))
obt=int(input("enter obtained marks:"))
print("your percentage is=",(obt*100)/ttl,"%")