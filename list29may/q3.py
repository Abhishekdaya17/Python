'''Industrial Sensor Peak Energy Monitoring System

Problem Statement

A factory machine records energy consumption at regular intervals.

A peak is defined as a value greater than or equal to its neighbors.

Tasks:

Find all peak energy values
Compute sum of squares of peak values
Compute average of peak values
Return difference between max peak and min peak
If no peaks, return -1

Test Case 13.


Input:
energy = [20, 40, 30, 60, 50]

Output:
Peaks = [40, 60]
Sum of squares = 5200
Average = 50
Difference = 20

Test Case 2

Input:
energy = [10, 20, 15, 25, 20, 30]

Output:
Peaks = [20, 25, 30]
Sum of squares = 1525
Average = 25
Difference = 10

Test Case 3

Input:
energy = [5]

Output:
Peaks = [5]
Sum of squares = 25
Average = 5
Difference = 0'''
product=1
peak=[]
sum=0
sum1=0
n=int(input("size of list:"))
a=[]
for i in range(n):
    str=int(input("energy:"))
    a.append(str)
print(a)
for i in range(0,n):
        ispeak=True
        if n==1 or i==0:
            if n==1:
                ispeak=True
            else:
                if a[i]>=a[i+1] :
                    ispeak=True
                else:
                    ispeak=False

                
        elif i==n-1:
            if a[i]>=a[i-1]:
                ispeak=True
            else:
                ispeak=False
        else:
            if a[i]>=a[i-1] and a[i]>=a[i+1]:
                    ispeak=True
            else:
                    ispeak=False
        if ispeak:
            peak.append(a[i])
            product=product*a[i]

            sum=sum+(a[i])**2
            sum1=sum1+a[i]
max=0
for i in peak:
     if i>max:
          max=i
min=peak[0]
for i in range(1,len(peak)):
     if peak[i]<min:
          min=peak[i]

print("peak elements:",peak)
print("sum of squares=",sum)
print("average=",sum1/len(peak))
print("max peak=",max)
print("min value=",min)
print("difference=",max-min)