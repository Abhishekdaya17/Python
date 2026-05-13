'''.
Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number

'''
num=int(input("input:"))
cub=num**3
a=cub%10
if a==num:
    print("trimorphic number")
else:
    print("not")