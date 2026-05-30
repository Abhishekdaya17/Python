'''4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]'''
n=int(input("number of values:"))
a=[]
for i in range(n):
    # str=map(str,input("enter the marks:").split())
    str=(input("enter the number"))
    a.append(str)
print(a) 
count=0
pall=[]
max=0
for i in a:
    if i==(i[::-1]):
        count=count+1
        pall.append(int(i))
        if int(i)>max:
            max=int(i)
           
        


    
    
print("pallindrome:",pall)
print(count) 
print("max pallindrome=",max)
print("sorted pallindrome:",sorted(pall))

