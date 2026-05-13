'''1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15'''

num=int(input("enter the number"))
mult=1
if num%2==0:
	for i in range(1,(num+1),2):
		mult=mult*i
else:
	for i in range(1,(num+1),2):
		mult=mult*i
print(mult)
