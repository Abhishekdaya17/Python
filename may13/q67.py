'''A
B B
C  C
D    D
EEEEEEEEE
'''
n=int(input("input:"))
for i in range(0,n):
    for s in range(0,n-i):
        print(" ",end="")
    for l in range(1,2*i):
        if l==1 or l==2*i-1:
            print(chr(i+64),end="")
        else:
            print(" ",end="")
    print()
for j in range(1,2*n):
    print(chr(64+n),end="")