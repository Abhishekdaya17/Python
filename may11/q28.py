'''28) Hollow Square
    *****
    *   *
    *   *
    *   *
    *****
'''
n=int(input("enter num:"))
num=(2*n)-1
i=1
while i<=n:
    print()
    if i==1 or i==n:
        for j in range(1,num+1,1):
            print("*",end="")
    else:
        for q in range(1,num+1,1):
            if q==1 or q==(num):
                print("*",end="")
            else:
                print(" ",end="")
                