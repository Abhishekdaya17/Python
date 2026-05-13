'''9.
 Bike Service Kilometer Checker

A bike needs service every 3000 km.

Write a program to:

- Read travelled kilometers
- Print every service checkpoint till entered km

Input:
10000

Output:
3000 6000 9000
'''
num=int(input("Input:"))
for i in range(3000,num+1,3000):
    print(i)
    if i>10000:
        break