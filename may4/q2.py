
'''2. Digit Sum Mirror Checker

A validation system checks symmetry in digit sums.

Write a program to:

Split number into two halves
Find sum of first half digits
Find sum of second half digits
Display both sums
If both sums are equal → print Balanced Number
Else → print Unbalanced Number

Input:
123321

Output:
First Half Sum = 6
Second Half Sum = 6
Balanced Number'''
num=int(input("input:"))

len=len(str(num))
power=len//2
half1=(num//(10**power))
half2=num-(half1*(10**power))
a=str(half1)
b=str(half2)
sum=0
sum2=0
for i in a:
    sum=sum+int(i)
for j in b:
    sum2=sum2+int(j)
print("first half sum",sum)
print("second half sum",sum2)
if sum==sum2:
    print("balance number")
else:
    print("not balanced")



