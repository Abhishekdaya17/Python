



'''
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number'''


'''num=int(input("input"))
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
diff=0
while rev>0:
    a=rev%10
    diff=abs(diff-a)
    print(diff,end=" ")
    rev=rev//10'''
    

n= input("Enter Number = ")
prev=0
diff=""
greater = 0
sum=0
for i in n:
    if prev==0:
        prev = int(i)
    else:
        diff=prev-int(i)
        sum+=abs(diff)
        

print(sum)