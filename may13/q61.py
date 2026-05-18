'''*
***
*****
*******
*********
'''
n=int(input("input:"))
for i in range(0,n+1):
    for s in range(0,n-i):
        print(" ",end="")
    for l in range(1,2*i):
        print("*",end="")
    print()
