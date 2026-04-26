'''6. Sum of Factors
A puzzle-based game rewards users based on the sum of all factors of a chosen number. The system calculates the total score using all factors of the entered number.
Write a program to find sum of factors using loops.

Input:
6

Output:
Sum = 12'''
num=int(input("enter the number:"))
sum=0
i=1
while i<=num:
    if num%(i)==0:
        sum=sum+i
    else:
        sum=sum+0
    i+=1
print(sum)