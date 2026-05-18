'''1
1 2
1  3
1   4
1  3
1 2
1
'''
n=int(input("input:"))
for i in range(1,n+1):

    for j in range(1,i+1):
        if j==1 or j==i:
         print(j,end="")
        else:
           print(" ",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        if j==1 or j==i:
            print(j,end="")
        else:
           print(" ",end="")
    print()