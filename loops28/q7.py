'''7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number'''
num=int(input("input:"))
a=0
rev=0
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    j=2
    while j<(sum+1//2):
        if sum%j==0:
            a="not lucky"
            break
        else:
            a="lucky number"
            break
    j=j+1

    
    num=num//10

print(sum)
print(a)

