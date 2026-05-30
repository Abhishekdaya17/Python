'''
2.
Smart City Traffic Peak Load Analyzer

Problem Statement

A smart city monitors traffic density at different time intervals in a day.

An element is called a peak traffic point if it is greater than or equal to its adjacent elements.

You are given an array traffic[] of size N.

Tasks:

Find all peak elements
Calculate the sum of all peak traffic values
Find the product of all peak traffic values
Return the maximum peak value

Note:
If only one element exists, it is the only peak.

Test Case 1

Input:
traffic = [10, 50, 30, 70, 60, 90, 80]

Output:
Peaks = [50, 70, 90]
Sum = 210
Product = 315000
Max Peak = 90

Test Case 2

Input:
traffic = [100, 200, 150, 180, 170]

Output:
Peaks = [200, 180]
Sum = 380
Product = 36000
Max Peak = 200

Test Case 3

Input:
traffic = [5]

Output:
Peaks = [5]
Sum = 5
Product = 5
Max Peak = 5'''
product=1
peak=[]
sum=0
n=int(input("size of list:"))
a=[]
for i in range(n):
    str=int(input("enter the traffic density:"))
    a.append(str)
print(a)
for i in range(0,n):
        ispeak=True
        if n==1 or i==0:
            if n==1:
                ispeak=True
            else:
                if a[i]>a[i+1] :
                    ispeak=True
                else:
                    ispeak=False

                
        elif i==n-1:
            if a[i]>a[i-1]:
                ispeak=True
            else:
                ispeak=False
        else:
            if a[i]>a[i-1] and a[i]>a[i+1]:
                    ispeak=True
            else:
                    ispeak=False
        if ispeak:
            peak.append(a[i])
            product=product*a[i]

            sum=sum+a[i]
max=0
for i in peak:
     if i>max:
          max=i
print("peak elements:",peak)
print("sum=",sum)
print("product=",product)
print("max peak=",max)