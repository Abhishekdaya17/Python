'''123456789
1234567
12345
123
1
'''
n=int(input("input:"))
for i in range(n):
    for j in range(0,i):
        print(" ",end="")
    for k in range(1,2*n-2*i):
        print(k,end="")
    print()