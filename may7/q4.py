'''4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407

'''
n1=int(input("enter starting number:"))
n2=int(input("enter ending number:"))
for i in range(n1,n2+1):
    a=i                   
    l=len(str(i))
    power=l
    sum=0
    while a>0:
        rem=a%10
        sum=sum+(rem**power)
        a=a//10
    if i==sum:
        print(i)
    
