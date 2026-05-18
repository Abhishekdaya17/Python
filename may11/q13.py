'''13) Number X Pattern
    1   5
     2 4
      3
     2 4
    1   5

'''
'''
n=int(input("input:"))
i=1


while i<=n:
    
    for j in range(1,i+1,1):
        if j==i:
            print(j,end="")
        else:
            print(" ",end="")


    for k in range(n,i,-1):
        print("  ",end="")
    for l in range(i,n+1,-1):
        if l==n:
            print(l,end="")
        else:
            print(" ",end="")

    print()
    i=i+1
o=n-1

while o>=1:
 
    
    for p in range(1,o+1,1):
        if p==o:
             print("*",end="")
        else:
            print(" ",end="")

    
    for q in range(n,o,-1):
        print("  ",end="")

    
    for s in range(o,0,-1):
        if s==o:
            print("*",end="")
        else:
            print(" ",end="")


    print()
    o=o-1'''
n = int(input("input:"))

for i in range(n):
    for j in range(n):

        if i == j:
            print(i + 1, end="")

        elif i + j == n - 1:
            print(n - i, end="")

        else:
            print(" ", end="")

    print()