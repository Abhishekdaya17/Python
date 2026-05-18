'''1
00
111
0000
11111
'''
n=int(input("input:"))
i=1
while i<=n:
    print()
    k=i+1
    for j in range(1,k):
        if i%2==1:
            print("1",end="")
        else:
            print("0",end="")
    i=i+1