'''4.

=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary Diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal

========================================================='''
r1=int(input("enter number of rows for for matrix1:"))
c1=int(input("enter number of columns for for matrix1:"))
                
print("enter the values for matrix")
matrix=[]
for i in range(r1):
        rows=[]
        for j in range(c1):
            s=int(input("enter the element"+str(j)+":"))
            rows.append(s)
        matrix.append(rows)
for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            print(matrix[m][n],end=" ")
        print()





while True:
    print('''
Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

    
        ''')
   
        
    n=int(input("enter the choice:"))
    d1=0
    d2=0
    match n:
            case 1:
                for i in range(len(matrix)):
                        for j in range(len(matrix[i])):
                            if i==j:
                                  print(matrix[i][j],end=" ")
                                  d1=d1+matrix[i][j]
                        print()
                
            case 2:
                for i in range(len(matrix)):
                        for j in range(len(matrix[i])):
                         if (i+j)==len(matrix)-1:
                             print(matrix[i][j],end=" ")
                             d2=d2+matrix[i][j]
                        print()
                        
            case 3:
                for i in range(len(matrix)):
                      for j in range(len(matrix[i])):
                            if i==j:
                                
                                  d1=d1+matrix[i][j]
                for i in range(len(matrix)):
                      for j in range(len(matrix[i])):
                        if (i+j)==len(matrix)-1:
                             
                             d2=d2+matrix[i][j]
                print("main diagonal sum=",d1)
                print("secondary diagonal sum=",d2)
                if d1==d2:
                        print("both diagonal are equal")
                else:
                      print("both are not equal")

            case 4:
                    print("Thank You for Using Matrix Diagonal Analysis System")
                    break
            case _:
                print("invalid choice")
    