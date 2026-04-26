'''*11. Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.

Input: Number = 122312, Digit = 2
Output: 3
'''
num=int(input("Input:="))
dig=int(input("digit:"))
count=0

while num>0:
    
    rem=num%10
    if dig==rem:
            count=count+1
    else:
        pass
    num=num//10
print(count)

