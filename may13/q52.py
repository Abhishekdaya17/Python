'''12345
1__4
1_3
12
1
'''
n=int(input("input:"))
for i in range(n,0,-1):
    for s in range(0,n-i,1):
        print(" ",end="")
    for j in range(1,i+1):
        if j==1 or j==i or i==n:

            print(j,end="")
        else:
            print("_",end="")
    print()
