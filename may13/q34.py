'''EEEEE
DDDD
CCC
BB
A'''	
n=int(input("input:"))
i=70
n=n+65
while i<=n:
    for j in range(i,n+1,1):
        print(chr(j),end="")
    print()
    i=i+1