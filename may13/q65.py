'''1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''
n=int(input("input:"))
for i in range(0,n):
    num=1
    for j in range(0,n-i-1):
        print(" ",end="")
    for k in range(i+1):
        print(num,end="")
    num=num*(i-j)//(j+1)
    print()
        
