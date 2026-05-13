'''9.
Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12

Output:
Abundant Number

'''
num=int(input("input:"))
count=0
for i in range(1,num,1):
    if num%i==0:
        count=count+i
    else:
        count=count+0
else:
    if count>num:
        print("abundant number")
    else:
        print("not abudent number")
              