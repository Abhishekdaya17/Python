'''21) Hollow Pyramid (Practice)
            *
           * *
          *   *
         *     *
        *********'''
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