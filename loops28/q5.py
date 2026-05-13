'''. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3
'''
num=int(input("input:"))
a=num
while True:
    j=2
    while j<=num:
        if num%j==0:
            break
        j=j+1
    if j>num//2:
        nextprime=num
        break
    num=num+1
print("next prime is",nextprime)
print("gap",nextprime-a)