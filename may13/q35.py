'''
*****
*  *
* *
**
*
'''
n=int(input("input:"))
for l in range(1,n+1):
      print("*",end="")
print()


i=1
while i<=n:
    
    for j in range(i,n+1):
        if j==i or j==n:
         print("*",end="")
        else:
            print(" ",end="")
    print()
    i=i+1
