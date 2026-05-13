'''10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime
'''
num=int(input("Input:"))
sum=0
count=0
smallest=9
totalsum=0


while num>0:
    rem=num%10
    sum=sum+rem
    if rem<smallest:
        smallest=rem
    if rem==0:
        count=count+1
    num=num//10
totalsum=sum+count
multi=smallest*totalsum
print("zero count:",count)
print("sum",sum)
print("smallest",smallest)
print("multiplication",multi)
if multi<=1:
    print("not prime")
else:
    j=2
    x=0
    while j<=(multi-1):
        if multi%j==0:
            x=1
            break
        j=j+1
    if x==1:
        print("not prime")
    else:
        print("prime")
    
             