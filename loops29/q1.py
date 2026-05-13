'''1. Triple Operation Prime Verification System

A cybersecurity company generates a security score from entered access code.

Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime


'''
num=int(input("input:"))
a=num
sum=0
rev=0
fn=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    sum=sum+rem
    num=num//10
print("sum of digits",sum)
print("reverse =",rev)
print("difference",abs(a-rev))
fr=sum+abs(a-rev)
print("final result",fr)
if fr<=1:
    print("not prime")
else:
    j=2
    while j<fr-1:
        if fr%j==0:
            break
        print("not prime")
        j=j+1
    else:
        print("prime")
        