r1=int(input("enter number of rows for for matrix1:"))
c1=int(input("enter number of columns for for matrix1:"))
r2=int(input("enter number of rows for for matrix2:"))
c2=int(input("enter number of columns for for matrix2:"))
if r1==r2 and c1==c2:
                matrix1=[]
                for i in range(r1):
                    rows=[]
                    for j in range(c1):
                        s=int(input("enter the element"+j+":"))
                        rows.append(s)
                    matrix1.append(rows)
                
                matrix2=[]
                for i in range(r2):
                    rows=[]
                    for j in range(c2):
                        s=int(input("enter the element:"))
                        rows.append(s)
                    matrix2.append(rows)
                result=[]
                for i in range(r1):
                    rows=[]
                    for j in range(c1):
                        s=matrix1[i][j]+matrix2[i][j]
                        rows.append(s)
                    result.append(rows)
                for i in range(matrix1):
                    print()
                    for j in range(len(matrix1[i])):
                        print(matrix1,end="")
else:
     print("not possible")
