'''
5. Count Factors of Number
A mathematics learning app gives practice questions where students must know how many factors a number has. The app should automatically count the total factors of the entered number.
Write a program to count total factors of a number using loops.

Input:
12

Output:
Factors Count = 6
'''
num=int(input("enter the number:"))
count=0
i=1
while i<=num:
    a=num%(i)
    if a%(i)==0:
        count=count+1
    else:
        count=count+0
    i+=1
print(count)