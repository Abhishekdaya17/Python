'''a
bc
d f
g  j
klmno
'''
n=int(input("input:"))
i=97
n=97+n
while i<=n-1:
    
    for j in range(97,i+1):
        if j==97 or j==i:
         print(chr(j),end=" ")
        else:
            print(" ",end=" ")
    print()
    i=i+1
for l in range(97,n+1):
      print(chr(l),end=" ")