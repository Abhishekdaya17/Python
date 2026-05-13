'''enter n6
     *
    **
   ***
  ****
 *****
******
'''
n=int(input("enter the number"))
i=1
while i<=n:
    print()
    
    k=n
    for j in range(k,i-1,-1):
        print(" ",end="")
        k=k-1
    for p in range(1,i+1,1):
        print("*",end="")
    i=i+1


    
      