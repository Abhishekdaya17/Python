'''A B C D E
A B C D
A B C
A B
A
'''
n=int(input("input:"))
for i in range(n):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,n-i):
        print(chr(k+65),end=" ")
    print()