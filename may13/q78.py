'''1
12
123
1234
123
12
1

'''
n=int(input("input:"))
for i in range(1,n+1):
    for s in range(0,n-i):
        print(" ",end="")

    for j in range(1,i+1):
        print(j,end="")
    print()
for i in range(n-1,0,-1):
    for s in range(0,n-i,1):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()