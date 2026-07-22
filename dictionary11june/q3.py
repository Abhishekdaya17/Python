# 3.

# =========================================
# WEBSITE PAGE VISIT TRACKER
# ==========================

# A website records page visits.

# pages = ["Home","About","Home","Contact","Home","About"]

# Write a program to:

# * Count visits of each page using a dictionary.
# * Display page name and visit count.

# Sample Output:
# Home visited 3 times
# About visited 2 times
# Contact visited 1 time

# ---
n=int(input("enter the size:"))
pr=[]

for i in range(n):
    s=input("enter the field of employee:")
    pr.append(s)
d={}
for j in pr:
    d[j]=d.get(j,0)+1
    
for k,v in d.items():
    print(k,"visited",v,"times")