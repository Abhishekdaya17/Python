'''7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32'''
num1,num2=map(int,input("Enter the num1 and num2").split())
res=1
for i in range(1,num2+1,1):
    res=res*num1

print(res)
    