'''1) Hollow Pyramid
        *    
       * *
      *   *
     *     *
    *********'''
'''n=int(input("enetr n"))
i=1
while i<=n:
    print()
    k=n
    for j in range(k,i,-1):
            print(" ",end="")
    print("*",end="")

    if i>=2:
            for p in range(1,i,1):
                print(" ",end="")
            if i==n:
                 print("*",end="")
            for q in range(i,1,-1):
                if q==2:
                    print("*",end="")
                else:
                    print(" ",end="")
            

    
    i=i+1'''
n=int(input("input:"))
for i in range(n-1):
    for s in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        if j==0 or j==2*i or i==n-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for k in range(1,n+1):
    print("*",end=" ")