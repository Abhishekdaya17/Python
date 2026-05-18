'''A
AB
A_C
A__D
ABCDE
'''
n=int(input("input:"))
n=n+65
i=65
while i<n:
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(65,i,1):
        if k==65 or k==i-1:
            print(chr(k),end="")
        else:
            print("_",end="")
    print()
    i=i+1
for m in range(65,n,1):
    
    print(chr(m),end="")