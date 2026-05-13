'''6.
Next Prime Cabin Number Generator

A luxury hotel gives only prime numbered cabins to VIP guests.

Manager enters the last allotted cabin number.
System must find the next available prime cabin number.

Write a program using loops.

Input:
24

Output:
Next Prime Cabin = 29

'''
num=int(input("input:"))
while True:
    num=num+1
    j=2
    while j<=num//2:
        if num%j==0:
            break
        j=j+1

    else:
        print("next prime",num)
        break
     

    
