'''7) Reverse Number Triangle
    - - - -
    2 - - -
    4 3 - -
    6 5 4 -
    8 7 6 5

'''
n=int(input("input:"))
i=0
while i<=2*n:
    for k in range(i,2*i,-1):
            print(k,end="")
    for j in range(i+1,n):
        print("-",end="")
    
    print()
    i=i+2