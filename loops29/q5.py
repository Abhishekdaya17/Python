'''5.Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number

'''

num=int(input("input"))
x=num%10
num=num//10
while num>0:
    rem=num%10
    if rem>x:
        print("unstable number")
        break
    x=rem
    num=num//10
else:
    print("stable")


#     x=num%10
#     if x>rem:
#         x=rem
#         print("stable")
#     elif x<=rem:
#         break
#     num=num//10

# else:
#     print("unstable")



    