'''5.

Automorphic Number Lock

A high-security digital locker validates access codes using a special mathematical rule.

When a user enters a numeric code, the system squares the number and checks whether the last digits of the square match the original number.
 If it matches, the code is considered valid.

An Automorphic Number is a number whose square ends with the same number.

Task:
Write a Python program to check whether a given number is an Automorphic Number or not.

Example:
Input:
25

Output:
Automorphic Number

num=input("input")
ov=int(num)
len=len(num)
power=1
a=int(num)
sqr=a**2
while a>0:
    bf=a//10**power
    remvalue=a-(bf*10**power)
    if remvalue==ov:
        print("automorphic number")
    else:
        print("not")
        power=power+1'''
num = input("Enter number: ")
n = int(num)

digits = len(num)
square = n * n

if square % (10 ** digits) == n:
    print("Automorphic Number")
else:
    print("Not Automorphic Number")



