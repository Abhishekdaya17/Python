'''4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
'''
num=int(input("input:"))
a=num

sum=0

for i in str(num):
    a=int(i)
    fact=1
    for i in range(a,0,-1):
        fact=fact*i
    sum=sum+fact
        
print(sum) 
# while num>0:
#     rem=num%10
#     print(rem)
#     j=1
#         while 
#          sum=sum+fact
#     print(sum)
#     num=num//10

# if a==sum:
#     print("strong number")
# else:
#     print("not strong")