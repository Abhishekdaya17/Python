'''5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''
n=int(input("input:"))
for i in range(n):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,n-i):
        print(n-i,end=" ")
    print()