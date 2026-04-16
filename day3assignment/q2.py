'''Assignment 2: Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000'''
iw,dy=map(int,input("Enter your daily wage and number of days :").split())
sal=iw*dy
print("your salary is:",sal)