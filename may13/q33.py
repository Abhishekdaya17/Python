'''ABCDE
ABCD
ABC
AB
A
'''


n=int(input("input:"))
i=65
n=n+65
while i<=n:
    for j in range(i,n+1,1):
        print(chr(j),end="")
    print()
    i=i+1
