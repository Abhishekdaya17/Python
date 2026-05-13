'''29) Diagonal Number Square
    1 - - -
    - 2 - -
    - - 3 -
    - - - 4
'''
n=int(input("input:"))
i=1
while i<=n:
    print()
    for j in range(1,n+1,1):
        if j==i:
            print(j,end="")
        else:
            print("-",end="")


    i=i+1
    