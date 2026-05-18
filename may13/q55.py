'''ABCDE
ABCD
ABC
AB
A
'''
n=int(input("input:"))
for i in range(n,0,-1):
    for s in range(0,n-i,1):
        print(" ",end="")
    for j in range(1,i+1):
        

            print(chr(64+j),end="")
        
    print()