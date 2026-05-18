'''*
*_*
*_*_*
*_*_*_*
*_*_*
*_*
*  
'''
n=int(input("input:"))
for i in range(1,2*n):
    for j in range(n,i-1,-1):
        print(" ",end="")
    if i%2==0:
        for u in range(2*n,i+2,-1):
            print("-",end=" ")
    else:
        for k in range(1,i+1):
            print("*",end=" ")
    print()
