'''7.
 Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345

Output:
Alternate Sum = 9
Not Prime
'''
num=int(input("input:"))
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
    rem=num%10
    sum=sum+0
    num=num//10
print(sum)    
if sum<=1:
    print("not prime")
else:
    j=2
    while j<=(sum+1)//2:
        if sum%j==0:
            print("not prime")
            break
        j=j+1
    else:
        print("prime")