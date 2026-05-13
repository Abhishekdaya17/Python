'''6) Number Triangle with Dashes
    - - - - 1
    - - - 2 3
    - - 3 4 5
    - 4 5 6 7
    5 6 7 8 9
'''
n=int(input("input:"))
i=1
while i<=n:
    for j in range(i,n):
        print("-",end="")
    for k in range(i,2*i,1):
            print(k,end="")
    print()
    i=i+1 