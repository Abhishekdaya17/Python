n = int(input("Enter n: "))

i = 1

while i <= n:

    # spaces
    j = 1
    while j <= n-i:
        print(" ", end="")
        j = j + 1

    # stars and hollow part
    k = 1
    while k <= (2*i)-1:

        if i == 1 or i == n:
            print("*", end="")

        else:
            if k == 1 or k == (2*i)-1:
                print("*", end="")
            else:
                print(" ", end="")

        k = k + 1

    print()

    i = i + 1
    n=int(input("input:"))
i=1
while i<=n:
    print()
    for j in range(1,i+1,1):
        print(j,end="")
    for k in range(n,i,-1):
        print(" ",end="")
    for l in range(n,i-1,-1):
        if l==i:
            for m in range(l,0,-1):
                 print(m,end="")
        else:
            print(" ",end="")
    i=i+1
o=1
while o<=n:
    print()
    for p in range(1,(n+1)-o,1):
        print(p,end="")
    for q in range(1,o,1):
        print(" ",end="")
    for r in range(0,o,1):
        print(" ",end="")
    for s in range(n-1,o-1,-1):
        print(s,end="")
    
    o=o+1