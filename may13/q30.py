'''***** 
**** 
***
**
* 
'''
n=int(input("input:"))
i=1
while i<=n:
    for j in range(n,i-1,-1):
        print("*",end="")
    print()
    i=i+1