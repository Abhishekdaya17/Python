'''1
22
333
4444
55555
'''
n=int(input("input:"))
i=1
while i<=n:
    for j in range(n,i-1,-1):
        print(" ",end="")
    for k in range(1,i+1,1):
        print(i,end="")
    print()
    i=i+1