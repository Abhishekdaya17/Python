
# 5.

# =========================================
# WORD LENGTH GROUPING
# ====================

# A content management system stores article tags.

# tags = ["python","java","api","react","html","css"]

# Write a program to:

# * Group words according to their length.
# * Store result in dictionary.

# Sample Output:
# {
# 3:['api','css'],
# 4:['java','html'],
# 5:['react'],
# 6:['python']
# }
n=int(input("enter the size:"))
pr=[]

for i in range(n):
    s=input("enter the field of employee:")
    pr.append(s)
g={}
for w in pr:
    l=len(w)
    if l not in g:
        g[l]=[]
    g[l].append(w)
print(g)
