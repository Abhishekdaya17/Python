# 6.

# =========================================
# MOBILE APP DOWNLOAD COUNTER
# ===========================

# Downloads received from different cities:

# cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

# Write a program to:

# * Count downloads city-wise.
# * Display city with maximum downloads.

# Sample Output:
# {'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
# Most Downloads : Indore

# ---
n=int(input("enter the size:"))
pr=[]

for i in range(n):
    s=input("enter the field of employee:")
    pr.append(s)
max=0
d={}
for j in pr:
    d[j]=d.get(j,0)+1
print(d)
name=""
for m,n in d.items():
    if n>=max:
        max=n
        name=m
print("most downloads=",name)



    
for k,v in d.items():
    print(k,"visited",v,"times")
