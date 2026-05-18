'''5
54
543
5432
54321
'''
n=int(input("input:"))
i=0
while i<n:
    print()
    k=i+1
    for j in range(n,(n-k),-1):
    
            print(j,end="")
    i=i+1