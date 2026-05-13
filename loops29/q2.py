'''2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime
'''
num=int(input("input:"))
sum=0
pro=1
count=0
while num>0:
    rem=num%10
    sum=sum+rem
    pro=pro*rem
    num=num//10
print("sum",sum)
print("product",pro)
diff=abs(sum-pro)
print("difference",diff)
a=diff

while diff>0:
    diff%10
    count=count+1
    diff=diff//10
print("diff digit",count)
fr=count+a
print("final result",fr)
if fr<=1:
    print("not primr")
else:
    j=2
    while j<=fr-1:
        if fr%j==0:
         print("not prime")
         break

        j=j+1
    else:
        print("prime")

