'''1. Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number
'''
num=int(input("Input:"))
x=0
if num<=1:
    print("Not prime")
i=2
while i<(num-1):
    if num%i==0:
        x=1
        break
    i=i+1
if x==1:
    print("not prime")
else:
    print("prime")


