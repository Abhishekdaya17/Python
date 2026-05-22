'''2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST'''
n=input("input:")
l=len(n) 
result=""
for i in range(0,l,1):
    ch=n[i]
    if i==0 or n[i-1]==" ":
        if n[i]>="a" and n[i]<="z":
            result=result+(chr(ord(ch)-32))
        else:
            result=result+ch
print(result)
