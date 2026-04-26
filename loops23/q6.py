'''6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong'''
num=int(input("Input:"))
a=num
sum=0
while num>0:
    rem=num%10
    sum=sum+(rem**3)
    num=num//10
if sum==a:
    print("armostrong")
else:
    print("not armstrong")