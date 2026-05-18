'''     1               
101            
10101         
1010101           
101010101   
10101010101
'''
n=int(input("input"))
for i in range(1,n+1):
    for s in range(1,(n-i)+1):
       print(" ",end="")
    for j in range(1,2*i):
        if j%2==1:
          print("1",end="")
        else:
           print("0",end="")
    print()
