'''WAP to find out all the leap years between two entered years'''
n1=int(input("enter starting year:"))
n2=int(input("eneter last year"))
for i in range(n1,n2):
     
    if (i%4==0 or i%400==0) and i%100!=0:
        print(i)


