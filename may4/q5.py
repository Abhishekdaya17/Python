'''5.
Tech Number Checker

A number is called a Tech Number if:

It has even number of digits
Split it into two equal halves
Add both halves
Square the sum
If result equals original number → Tech Number

Write a program to:

Count digits
If digits are even, split the number
Find sum of both halves
Square the sum
Display intermediate values
Check and print result

Input:
2025

Output:
First Half = 20
Second Half = 25
Sum = 45
Square = 2025
Tech Number'''
num=int(input("enter the number:"))
str1=str(num)
lenght=len((str1))
if lenght%2==0:
    l=len(str(num))
    power=lenght//2
    num1=num//(10**power)
    print("first half",num1)
    num2=num-(num1*(10**power))
    print("second half",num2)
    sum=num1+num2
    print("sum=",sum)
    sqr=sum**2
    print("square=",sqr)
    if num==sqr:
        print("tech number")
    else:
        print("not tech numbr")
else:
    print("plese enter even number")

