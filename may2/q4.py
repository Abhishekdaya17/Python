'''4.
1. Digit Gap Consistency Checker

A number analysis system checks whether the gap between digits follows a consistent pattern.

Write a program to:

Find the absolute difference between first two digits
Compare this difference with all next adjacent digit differences
If any difference is not equal to the first difference, stop using break
Display:
- Initial gap
- Whether all gaps are same or not

Input:
8642

Output:
Initial Gap = 2
Consistent Pattern

Input:
97531

Output:
Initial Gap = 2
Consistent Pattern

Input:
5321

Output:
Initial Gap = 2
Pattern Break Detected

'''
num=input("input:")
len=len(num)
power=len-1
a=int(num)//10**power
num1=int(num)%(10**power)
diff1=abs(int(num[0])-int(num[1]))
q="consitent"
for i in str(num1):
    b=int(i)
    diff=abs(a-b)
    if diff!=diff1:
        q="pattern breaked"
        break
    a=b
print("initial gap=",diff1)
print(q)

