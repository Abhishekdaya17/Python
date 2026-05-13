'''
9) Hollow Diamond Square
    ***********
    ****   ****
    ***     ***
    **       **
    *         *
    *         *
    **       **
    ***     ***
    ****   ****
    ***********'''
n=int(input("input:"))
i=1
o=i
while i<=n:
    print()
    for j in range(n,i-1,-1):
        print("*",end="") 
    for m in range(1,i,1):
        print(" ",end="")
    for z in range(1,i,1):
        print(" ",end="")
    for x in range(n+1,i,-1):
        print("*",end="")
    i=i+1
k=1
while k<=n:
    print()
    for l in range(1,k+1,1):
        print("*",end="")
    for w in range(n,k,-1):
        print(" ",end="")
    for y in range(n,k,-1):
        print(" ",end="")
    for q in range(1,k+1):
        print("*",end="")
    k=k+1

