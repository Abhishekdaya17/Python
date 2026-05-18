'''123456789
1+++++7
1+++5
1+3
1
'''
n=int(input("input:"))
start=2*n-1
for l in range(1,start+1):
    print(l,end="")
print()
for i in range(1,n):
    for j in range(0,i):
        print(" ",end="")
    for k in range(1,start-2*i+1):
        if k==1 or k==start-2*i:
            print(k,end="")
        else:
            print("+",end="")
    print()