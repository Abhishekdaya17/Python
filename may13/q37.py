'''*****
####
***
##
*'''

n=int(input("input:"))
i=1
while i<=n:
    for j in range(i,n+1,1):
        if i%2==0:
            print("#",end="")
        else:
            print("*",end="")
    print()
    i=i+1