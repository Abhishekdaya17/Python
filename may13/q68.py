'''#
*#* 
**#** 
***#*** 
****#****
'''
n=int(input("input:"))
for i in range(n):
    for k in range(0,n-i,1):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print("#",end="")
    for l in range(0,i):
        print("*",end="")
    print()
