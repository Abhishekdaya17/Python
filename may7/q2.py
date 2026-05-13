'''2.
Perfect Number Analyzer

A mathematics research system analyzes special numbers within a given range.
The user enters a starting number and ending number.
The system checks every number in that range and displays all Perfect Numbers using nested loops.

(A Perfect Number is a number whose sum of proper divisors is equal to the number itself.)

Input:
Enter starting number: 1
Enter ending number: 1000

Output:
Perfect Numbers are:
6
28
496
'''
n1=int(input("enter starting number:"))
n2=int(input("enter ending number:"))

for i in range(n1,n2+1,1):
    a=i
    sum=0

    for j in range(1,(a//2)+1,1):
        if a%j==0:
            sum=sum+j
    if sum==i:
        print(i)
        
