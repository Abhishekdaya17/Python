'''A
AB
A C
A  D
ABCDE
'''
n=int(input("input:"))
i=65
n=65+n
while i<=n-1:
    
    for j in range(65,i+1):
        if j==65 or j==i:
         print(chr(j),end=" ")
        else:
            print(" ",end=" ")
    print()
    i=i+1
for l in range(65,n+1):
      print(chr(l),end=" ")