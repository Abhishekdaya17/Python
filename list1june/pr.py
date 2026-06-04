''''''
rows=int(input("enter the number of rows="))
cols=int(input("enter the number of columns="))
banda=int(input("enter element to search:"))
mat=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        s=int(input("enter the element"+str(j)+":"))
        row.append(s)
    mat.append(row)

print(mat)
sum1=0
x=0
for i in range(len(mat)):
       
    for j in range(len(mat[i])):
              ch=mat[i][j]
              print(ch,end=" ")
    print()
print("rverse")  
for rows in mat:
      rows.reverse()
for i in range(len(mat)):
    rev=[]
       
    for j in range(len(mat[i])):
              ch=mat[i][j]
              print(ch,end=" ")
    print()  
        
        
              
                   


            

        