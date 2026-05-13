'''3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35'''
num1,num2=map(int,input("input").split())
count=0
if num1<num2:
    for i in  range(num1,num2+1,1):
        if i%10==5:
            print(i,end=" ")
elif num1>num2:
    num1,num2=num2,num1
    for i in  range(num1,num2+1,1):
        if i%10==5:

            print(i,end=" ")

else:
    print("both are same number")

