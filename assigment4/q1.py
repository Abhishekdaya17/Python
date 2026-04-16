
'''Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75'''
ttb,gst,sc,nf=map(int,input("Total bill amount ,GST ,service charge and number of friend").split())
fb=((ttb*(gst+sc))/100)+ttb
ph=fb/nf
print("Final bill :",fb,"\n","Each Person Pays=",ph)