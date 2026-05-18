'''A
BCD
EFGHI
JKLMNOP
'''
n=int(input("input:"))
n=n+65
i=65
stop=2

while i<=n:

    
    for j in range(i,stop+64,1):
        print(chr(j),end="")

    stop=stop+2
    print()
    i=i+1