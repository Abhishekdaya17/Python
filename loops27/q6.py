'''6. Automorphic Number Checker

A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.

Input:
25

Output:
Automorphic Number'''
a=int(input("Input:"))
sqr=a**2
print(sqr)
str1=str(sqr)
power=len(str1)-1
print(power)
fn=sqr//(10**power)
print(fn)
b=sqr-(fn*(10**power))
print(b)
if a==b:
    print("automorphic number")
else:
 print("not")




