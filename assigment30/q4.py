'''4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number'''
num=int(input("input:"))
sum=0
pro=1
while num>0:
    rem=num%10
    sum=sum+rem
    pro=pro*rem
    num=num//10
if sum==pro:
    print("spy number")
else:
    print("not")
