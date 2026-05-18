'''ABCDE
A__D
A_C
AB
A
'''
n=int(input("input:"))
for i in range(n,0,-1):
    for s in range(0,n-i,1):
        print(" ",end="")
    for j in range(1,i+1):
        if j==1 or j==i or i==n:

            print(chr(64+j),end="")
        else:
            print("_",end="")
    print()
