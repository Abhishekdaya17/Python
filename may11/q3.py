'''3) X Star Pattern
    *   *
     * *
      *
     * *
    *   *
'''
n=int(input("input:"))
i=1


while i<=n:
    
    for j in range(1,i+1,1):
        if j==i:
            print("*",end="")
        else:
            print(" ",end="")


    for k in range(n,i,-1):
        print("  ",end="")
    for l in range(i,0,-1):
        if l==i:
            print("*",end="")
        else:
            print(" ",end="")

    print()
    i=i+1
o=n-1

while o>=1:
 
    
    for p in range(1,o+1,1):
        if p==o:
             print("*",end="")
        else:
            print(" ",end="")

    
    for q in range(n,o,-1):
        print("  ",end="")

    
    for s in range(o,0,-1):
        if s==o:
            print("*",end="")
        else:
            print(" ",end="")


    print()
    o=o-1


