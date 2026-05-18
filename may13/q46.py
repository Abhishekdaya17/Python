'''A
AB
ABC
ABCD
ABCDE
'''

n=int(input("input:"))
n=n+65
i=65
while i<=n:
    for j in range(n,i-1,-1):
        print(" ",end="")
    for k in range(65,i,1):
        print(chr(k),end="")
    print()
    i=i+1