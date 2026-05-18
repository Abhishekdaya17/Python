'''*
  *_* 
 *___* 
*_____*
 *___* 
  *_*
   *
'''
n=int(input("input:"))
for i in range(1,n+1):
    for j in range(1,(n-i)+1,1):
        print(" ",end="")
    for k in range(1,2*i):
        if k==1 or k==2*i-1:
            print("*",end="")
        else:
            print("_",end="")
    print()
for i in range(1,n):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(1,n-i):
        if k==1 or k==n-i+1:
            print("*",end="")
        else:
            print("_",end="")
    print()
