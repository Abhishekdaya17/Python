'''123456
54321
1234
321
12
1
'''
n=int(input("input:"))
i=n
while i>0:
    if i%2!=0:
        for j in range(i,0,-1):
            print(j,end="")
    else:
         for k in range(1,i+1,1):
             print(k,end="")
    print()
    i=i-1
             