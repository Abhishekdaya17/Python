'''1) Hollow Pyramid
        *    
       * *
      *   *
     *     *
    *********'''
n=int(input("enetr n"))
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
            if i==n:
                     print("*",end="")
    
    i=i+1