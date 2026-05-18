'''1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
n=int(input("input:"))
for i in range(0,n+1):
    for s in range(0,n-i):
        print(" ",end="")
    for l in range(1,i+1):
        print(l,end=" ")
    print()