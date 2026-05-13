'''1)	WAP to find out the sum of all integer between 100 and 200 which are divisible by 9'''
n1=int(input("enter starting number:"))
n2=int(input("enter second number:"))
for i in range(n1,n2+1):
    if i%9==0:
        print(i)