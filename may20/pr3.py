''''''
n=int(input("inpu:"))
i=1
for j in range(1,n+1):
    print()
    if j==1 or j==n:
        for k in range(1,n+1):
            print("|",)
    if i==1 or i==n:
        for l in range(1,n+1):
            print("-",end="")