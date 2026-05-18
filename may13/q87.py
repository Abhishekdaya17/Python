'''***** *****
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
***** *****
'''
n=int(input("input:"))
for i in range(1,n+1):
    for j in range(0,(n-i)+1):
        print("*",end="")
    for k in range(1,i,1):
        print("  ",end="")
    for l in range(0,(n-i)+1):
        print("*",end="")
    print()

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    for k in range(n,i,-1):
        print("  ",end="")
    for l in range(1,i+1):
        print("*",end="")
    print()