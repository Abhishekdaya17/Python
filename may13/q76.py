'''x
xx
xxx
xxxx
xxx
xx
x
'''
n=int(input("input:"))
for i in range(1,n+1):
    print("x"*i)
for j in range(n-1,0,-1):
    print("x"*j)