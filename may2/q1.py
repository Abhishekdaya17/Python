'''1.Digit Product Analyzer System

A data analytics company studies patterns in numeric transaction IDs to detect hidden behaviors.

For every entered number, the system analyzes relationships between its digits.

Write a program to:

Find the product of every pair of adjacent digits
Display all the products
Find the sum of all these products
Find the smallest product value
If the sum of products is divisible by the total number of digits, print Stable Number
Otherwise print Unstable Number

Use loops wherever require

Input:
57294

Output:
Products: 35 14 18 36
Sum = 103
Smallest = 14
Unstable Number

'''
num=input("Input:")
len=len(num)
a=int(num)//10**(len-1)
num1=int(num)%((10**(len-1)))
num2=str(num1)
print(num2,type(num2))
sum=0

x=int(num2)
for i in num2:
    b=int(i)
    pro=int(a)*int(i)
    if int(pro)<x:
        x=pro



    sum=sum+pro

    print(pro,end=" ")
    a=b

print("sum is:",sum)
print("smallest product is:",x)
if sum%len==0:
    print("stable number")
else:
    print("unstable number")