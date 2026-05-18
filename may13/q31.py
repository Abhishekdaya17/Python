'''12345
1234
123
12
1
'''
n=int(input("input:"))
i=1
while i<=n:
    for j in range(i,n+1,1):
        print(j,end="")
    print()
    i=i+1