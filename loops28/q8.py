'''8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime

'''
num=int(input("input:"))
largest=0
smallest=9
sum=0
x=0
while num>0:
    rem=num%10
    if rem>largest:
        largest=rem
        
    if smallest>rem:
        smallest=rem
    num=num//10
sum=largest+smallest
j=2

while j<=(sum+1)//2:
    if sum%j==0:
        x=x+1
        break
    if j>(sum+1)//2:
        x=x+0
        break
    j=j+1
        
print(largest)
print(smallest)
print(sum)
if x==0:
    print("prime")
else:
    print("not prime")
                