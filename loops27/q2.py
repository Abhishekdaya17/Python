'''2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4
'''
num1,num2=map(int,input("input").split())
count=0
if num1<num2:
    for i in range(num1,num2+1,1):
        if i%7==0:
            count=count+1
        else:
            pass
elif num1>num2:
    num1,num2=num2,num1
    for i in range(num1,num2+1,1):
        if i%7==0:
            count=count+1
        else:
            pass
else:
    print("both are same")
print(count)
