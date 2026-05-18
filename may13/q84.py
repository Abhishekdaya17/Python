'''1
212
32123
4321234
543212345
'''

n=int(input("input:"))
for i in range(1,n+1):
    for s in range(n,i,-1):
        print(" ",end="")
    for j in range(i,0,-1):
        print(j,end="")
    for k in range(2,i+1):
        print(k,end="")
    print()
