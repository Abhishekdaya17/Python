# 2.

# =========================================
# EMPLOYEE DEPARTMENT COUNT
# =========================

# A company stores employee department names in a list.

# employees = ["HR","IT","HR","Sales","IT","IT","Finance"]

# Write a program to:

# * Count how many employees belong to each department.
# * Store the result in a dictionary.

# Sample Output:
# {'HR': 2, 'IT': 3, 'Sales': 1, 'Finance': 1}
n=int(input("enter the size:"))
pr=[]

for i in range(n):
    s=input("enter the field of employee:")
    pr.append(s)
d={}
for j in pr:
    d[j]=d.get(j,0)+1
    
print(d)
