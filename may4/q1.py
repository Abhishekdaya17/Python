'''1. Adjacent Digit Difference Analyzer

A system analyzes differences between consecutive digits in a number.

Write a program to:

Find the difference between every pair of adjacent digits
Display all differences
Count how many differences are even
Find the largest difference
If all differences are same → print Uniform Difference
Else → print Non-Uniform Pattern

Input:
84261

'''
num=int(input("enter number:"))
count=0
max=0
x=str(num)
len=len(str(x))
a=num//(10**(len-1))
rnum=(num-(a*(10**(len-1))))

d=None
diff = ""
for i in str(rnum):
    b=int(i)
    c=abs(a-b)
    diff=str(c)+diff
    print()
    if max<c:
        max=c
    if d==None:
        d=c
    
    
    if c%2==0:
        count=count+1

    if d==None:
        d=c
    else:
        if d!=c:
           p=("NOT EQAUL")
            
        else:
            p=("uniform")
    
    a=b

print()
print("Differences =",diff,)
print("max",max)
print("even difference ",count)
print(p)
    

