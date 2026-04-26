'''*7. Count Even Digits*
A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to *count the number of even digits in a given number using loops*.

Input: 123456
Output: Even digits count = 3
'''
num=int(input("Input:="))
count=0
while num>0:
    
    rem=num%10
    if rem%2==0:
           count=count+1
    else:
           count=count+0
    num=num//10
print("even digits are ",count)