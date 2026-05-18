'''55555
4  4
3 3
22
1
'''

n=int(input("input:"))

for l in range(1,n+1):
      print(n,end="")
print()
i=n-1
while i>0:
    for j in range(1,i+1,1):
            if j==1 or j==i:
                  print(i,end="")
            else:
                  print(" ",end="")
    print()              
    i=i-1              

    
      