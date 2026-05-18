'''1
11
1*1
1**1
11111
'''
n=int(input("input:"))
i=1

while i<n:
    x=i-1
    for j in range(n,i-1,-1):
        print(" ",end="")
    
    for l in range(1,i+1,1):
        if l==1 or l==i:
            print(1,end="")
        else:
            print("*",end="")
    
    

    
    print()
    i=i+1
for m in range(1,n+2,1):
    if m==1:
        print(" ",end="")
    else:
        print(1,end="")
