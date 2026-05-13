'''5. Digit Alternating Sum System

A coding system calculates alternating sum of digits (add, subtract, add...).

Write a program to:

Traverse digits from left to right
Add first digit, subtract second, add third, and so on
Display final alternating sum
If result is positive → print Positive Pattern
Else → print Negative Pattern

Input:
1234

Output:
Result = -2
Negative Pattern

Input:
8642

Output:
Result = 8
Positive Pattern'''
'''
num=input("input:")
num1=int(num)
lenght=len(num)
power=lenght-1
sum=0
while num1>0:
    rem=num1//10**power
    sum=sum+rem
    num1=num1-(rem*(10**power))
    rem1=num1//10**(power-1)
    sum=sum-rem1
    num1=num1-(rem1*(10**(power-2)))
num1=num1//10
print(sum)'''
num=input("input")
mult=1
sum=0
for i in num:
    sum=sum+(int(i)*mult)
    mult=mult*(-1)
if sum>0:
    print("positive pattern")
else:
    print("negative pattern")