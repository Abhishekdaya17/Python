'''5
44
333
2222
11111
'''
n=int(input("input:"))
i=1

while i<=n:
    x=i-1
    for j in range(n,i-1,-1):
        print(" ",end="")
    
    for l in range(n-x,n-i,-1):
        w=l
        for m in range(n,n-i,-1):
            print(w,end="")
    print()
    i=i+1