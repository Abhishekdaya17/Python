'''7.
Adam Number Verification System – Question

A high-security digital system is designed to validate special mirrored numbers known as Adam Numbers before granting access to sensitive data.

When a user enters a numeric code, the system performs a dual verification process:

* It calculates the square of the entered number.
* It reverses the number and calculates the square of the reversed value.
* Finally, it checks whether both results are mirror images (reverses) of each other.

A number is called an Adam Number if:
The square of the number and the square of its reverse are reverses of each other.

Task:
Write a Python program to check whether a given number is an Adam Number or not.

Examples:

Input:
12
Output:
Adam Number

Input:
13
Output:
Not an Adam Number

Input:
11
Output:
Adam Number

Example:
12 → 12² = 144, reverse(12) = 21 → 21² = 441 → reverse of 144

'''
num=int(input("input:"))
on=0
rev=0
sqr=num*num
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
revsqr=rev*rev
while revsqr>0:
    rev1=revsqr%10
    on=on*10+rev1
    revsqr=revsqr//10
else:



    if on==sqr:
        print("adam")
    else:
        print("not adam")