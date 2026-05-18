'''12) Hollow Diamond Numbers
       1
      2 2
     3   3
    4     4
     3   3
      2 2
       1
'''
'''n=int(input("input:"))
i=1
o=i
while i<=n:
    print()
    for j in range(n,i-1,-1):
        if j==i:
            print(j,end="")
        else:
            print(" ",end="")
    for m in range(1,i,1):
            print("*",end="")
    for z in range(1,i,1):
        print(z,end="")
    if i>=2:
        for x in range(n+1,i,1):

                print(" ",end="")
    i=i+1
k=1
while k<=n:
    print()
    for l in range(1,k+1,-1):
        print(" ",end="")
    for w in range(n,k,-1):
        if w==k-1:
            print(w,end="")
        else:
             print(" ",end="")
    for y in range(n,k,-1):
        print(" ",end="")
    for q in range(1,k+1):
        print("*",end="")
    k=k+1'''
n = int(input("input:"))

for i in range(1, n + 1):

    for s in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print(i, end="")
        else:
            print(" ", end="")
    print()

for i in range(n - 1, 0, -1):

    for s in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print(i, end="")
        else:
            print(" ", end="")
    print()