'''7) Reverse Number Triangle
    - - - -
    2 - - -
    4 3 - -
    6 5 4 -
    8 7 6 5

'''
n=int(input("input:"))
i=1
while i<=n:
    print()
    j=i
    k=2*(i-1)
    while j>1:
        print(k,end="")
        k=k-1
        j=j-1
    j=n
    while j>i:
        print("-",end="")
        j=j-1
    i=i+1