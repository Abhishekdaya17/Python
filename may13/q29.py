'''1
222
33333
4444444
555555555'''
n=int(input("input:"))
i=1
count=1
while i<=n:
    for j in range(1,count+1,1):
        print(i,end="")
    print()
    count=count+2
    i=i+1
