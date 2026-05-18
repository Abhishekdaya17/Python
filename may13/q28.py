'''1
123
12345
1234567
123456789
'''
n=int(input("input:"))
i=1
while i<=2*n-1:
    for j in range(1,i+1,1):
        print(j,end="")
    print()
    i=i+2
