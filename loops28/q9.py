'''9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
'''
num=int(input("input:"))
evencount=0
oddcount=0
while num>0:
    rem=num%10
    if rem%2==0:
        evencount=evencount+1
    else:
        oddcount=oddcount+1
    diff=abs(evencount-oddcount)
    num=num//10
print("even count",evencount)
print("odd count",oddcount)
print("diff",diff)
x=0
if diff<=1:
        print("not prime")

else:
    i=2
    while i<=diff//2:
        if diff%i==0:
            x=1
            break
        i=i+1
                    
    if x==0:
            print("prime")
    else:
            print("not prime")


            

