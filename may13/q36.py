'''
ABCDE
A  D
A C
AB
A
'''
n=int(input("input:"))
n=(n+65)-1
for l in range(65,n+1):
      print(chr(l),end="")
print()


i=65
while i<=n-1:
    last=(n+65)-i-1
    
    for j in range(65,last+1):
        if j==65 or j==last:
         print(chr(j),end="")
        else:
            print(" ",end="")
    print()
    i=i+1