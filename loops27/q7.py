'''7. Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number'''
num=int(input("input"))
rev=0

while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
a=rev%10
if a==0:
    out="rejected"
rev=rev//10

while rev>0:
        rem1=rev%10
        if rem1==0:
            out="duck number"
        rev=rev//10
print(out)
