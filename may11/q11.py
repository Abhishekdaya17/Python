n=int(input("input:"))
i=1


while i<=n:
    
    for j in range(1,i+1,1):
        print(j,end="")


    for k in range(n,i,-1):
        print("**",end="")
    for l in range(i,0,-1):
        print(l,end="")

    print()
    i=i+1
o=n-1

while o>=1:
 
    
    for p in range(1,o+1,1):
        print(p,end="")

    
    for q in range(n,o,-1):
        print("**",end="")

    
    for s in range(o,0,-1):
        print(s,end="")


    print()
    o=o-1