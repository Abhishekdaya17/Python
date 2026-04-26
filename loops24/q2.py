'''2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2'''
num=int(input("enter the number"))
len=len(str(num))
large=9

while num>0:
    digit = num%10
    if digit<large:
        large=digit
    num=num//10
print("smallest number = ",large)
