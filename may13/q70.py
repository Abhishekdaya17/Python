'''* * * * * 
* * * * 
* * * 
* * 
*
'''
n=int(input("input:"))
for i in range(n):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,n-i):
        print("*",end=" ")
    print()