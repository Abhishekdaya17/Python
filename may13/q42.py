'''54321
5432
543
54
5
'''
n=int(input("input:"))
i=1
while i<=n:
    for j in range(n,i-1,-1):
        print(j,end="")
    print()
    i=i+1