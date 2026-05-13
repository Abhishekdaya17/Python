'''WAP to print Square, Cube and Square Root of all numbers from 1 to N'''
n1=int(input("enter the number:"))
for i in range(1,n1+1):
    print("number=",i)
    print("square=",i**2)
    print("cube=",i**3)
    print("square root=",round(float(i**0.5),3))
    print()
