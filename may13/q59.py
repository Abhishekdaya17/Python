'''A
A B
A B C
A B C D
A B C D E  
'''
n=int(input("input:"))
for i in range(0,n+1):
    for s in range(0,n-i):
        print(" ",end="")
    for l in range(1,i+1):
        print(chr(l+64),end=" ")
    print()