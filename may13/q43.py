'''1
12
123
1234
12345
'''


n=int(input("input:"))
i=1
while i<=n:
    for j in range(n,i-1,-1):
        print(" ",end="")
    for k in range(1,i+1,1):
        print(k,end="")
    print()
    i=i+1