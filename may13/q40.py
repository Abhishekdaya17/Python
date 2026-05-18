'''
*
**
****
*******
***********
'''
n=int(input("input:"))
i=1
stop=i+1
while i<=n:
    
    for j in range(1,stop,1):
        print("*",end="")
    stop=stop+i
    print()
    i=i+1