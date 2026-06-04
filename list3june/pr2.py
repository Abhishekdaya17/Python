# r1=int(input("enter number of rows for for matrix1:"))
# c1=int(input("enter number of columns for for matrix1:"))
# r2=int(input("enter number of rows for for matrix2:"))
# c2=int(input("enter number of columns for for matrix2:"))
# if r1==r2 and c1==c2:
#                 print("enter the values for matrix1")
#                 matrix1=[]
#                 for i in range(r1):
#                     rows=[]
#                     for j in range(c1):
#                         s=int(input("enter the element"+str(j)+":"))
#                         rows.append(s)
#                     matrix1.append(rows)
#                 print("enter the values for matrix1")
#                 matrix2=[]
#                 for i in range(r2):
#                     rows=[]
#                     for j in range(c2):
#                         s=int(input("enter the element:"))
#                         rows.append(s)
#                     matrix2.append(rows)
#                 result=[]
#                 for i in range(r1):
#                     rows=[]
#                     for j in range(c1):
#                         s=matrix1[i][j]+matrix2[i][j]
#                         rows.append(s)
#                     result.append(rows)
#                 print("matrix1")
#                 for i in range(len(matrix1)):
                
#                     for j in range(len(matrix1[i])):
#                         print(matrix1[i][j],end=" ")
#                     print()
#                 print()
#                 print("matrix2")
#                 for i in range(len(matrix2)):
                    
#                     for j in range(len(matrix2[i])):
#                         print(matrix2[i][j],end=" ")
#                     print()
#                 print()
#                 print("resulu")
#                 for i in range(len(result)):
                    
#                     for j in range(len(result[i])):
#                         print(result[i][j],end=" ")
#                     print()
# else:
#      print("not possible")
r1=int(input("enter number of rows for for matrix1:"))
c1=int(input("enter number of columns for for matrix1:"))
            
print("enter the values for matrix1")
matrix=[]
for i in range(r1):
                                rows=[]
                                for j in range(c1):
                                    s=int(input("enter the element"+str(j)+":"))
                                    rows.append(s)
                                matrix.append(rows)

for i in range(c1):
                for j in range(r1):
                          print(matrix[i][j],end=" ")
                        
                print()
for i in range(c1):
                sum=0
                for j in range(r1):
                          sum=sum+matrix[j][i]
                print("sum of column"+str(i+1)+":",sum)
                        
                print()
                