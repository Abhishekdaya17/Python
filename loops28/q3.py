'''3. Composite Number Detector

A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number

'''
'''num=int(input("input:"))
if num==1:
  print("niether composite nor prime")
else:
    i=2
    while i<(num+1)//2:
     if  num%i==0:
        print("composite number")
        break
    else:
        print("not composite")
      break
    i=i+1'''
num=int(input("Input:"))
x=0
if num<=1:
    print("Not prime")
i=2
while i<(num-1):
    if num%i==0:
        x=1
        break
    i=i+1
if x==1:
    print("composite")
else:
    print("npt composite")


