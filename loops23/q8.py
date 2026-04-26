'''*8. Count Odd Digits*
A banking system flags IDs with too many odd digits for further verification.
Write a program to *count the number of odd digits in a given number using loops*.

Input: 123456
Output: Odd digits count = 3'''
num=int(input("Input:="))
count=0
while num>0:
    
    rem=num%10
    if rem%2==0:
           count=count+0
    else:
           count=count+1
    num=num//10
print("odd digits ",count)