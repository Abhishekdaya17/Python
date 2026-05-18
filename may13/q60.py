'''X 
X X 
X__X
X____X
X X X X X
'''
n=int(input("input:"))
for i in range(0,n):
    for s in range(0,n-i):
        print(" ",end="")
    for l in range(1,i+1):
        if l==1 or l==i:
            print("X",end=" ")
        else:
            print("_",end=" ")
    print()
for m in range(0,n,1):
    print("X",end=" ")