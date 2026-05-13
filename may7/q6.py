'''6.
Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191
'''
n1=int(input("enter starting number:"))
n2=int(input("enter the ending:"))
for i in range(n1,n2+1):
    a=i
    rev=0
    while a>0:
        rem=a%10
        rev=rev*10+rem
        a=a//10
    if i==rev:
        print(i)