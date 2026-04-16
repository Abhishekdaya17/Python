'''Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2s
Seconds = 30

Output:
Total Seconds = 3750'''
hr,mn,sc=map(int,input("enter time in hours minute and second:").split(" "))
print("your time in second:",hr*3600+mn*60+sc*1)