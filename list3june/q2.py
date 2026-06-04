'''2.

=========================================================
            MATRIX ANALYSIS SYSTEM
=========================================================


A research laboratory stores experimental data in matrix form.
Scientists want a program that can analyze the matrix and provide
different statistics through a menu-driven application.

The application should allow the user to:

1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Prime Numbers Row-wise
   2. Count Perfect Numbers Column-wise
   3. Display Row-wise Sum
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Prime Numbers Row-wise
   ---------------------------------------
   Count and display the number of prime numbers present
   in each row of the matrix.

5. Choice 2 - Count Perfect Numbers Column-wise
   --------------------------------------------
   Count and display the number of perfect numbers present
   in each column of the matrix.

   Note:
   A perfect number is a number that is equal to the sum
   of its proper divisors.

   Examples:
   6  = 1 + 2 + 3
   28 = 1 + 2 + 4 + 7 + 14

6. Choice 3 - Display Row-wise Sum
   --------------------------------
   Calculate and display the sum of each row.

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
2 4 5
6 7 8
11 28 13

Output:
Row 1 Prime Count = 2
Row 2 Prime Count = 1
Row 3 Prime Count = 2

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 2

Output:
Column 1 Perfect Number Count = 1
Column 2 Perfect Number Count = 1
Column 3 Perfect Number Count = 0

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 3

Output:
Row 1 Sum = 11
Row 2 Sum = 21
Row 3 Sum = 52

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Analysis System

=========================================================


'''
i=1
while i<=4:
    print('''  
    
Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit''')
    n=int(input("Enter your choice:"))
    match n:
        case 1:
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
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                          print(matrix[i][j],end=" ")
                print()
            
            for k in range(len(matrix)):
                primecount=0
                for l in range(len(matrix[i])):
                        num1=matrix[k][l]
                        
                        count=0
                        if num1>1:
                            for m in range(1,num1+1):
                                    if num1%m==0:
                                            count=count+1
                            if count==2:
                                primecount=primecount+1
                print("prime numbers count for row"+str(i+1)+":",primecount)
        case 2:
                  
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
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                          print(matrix[i][j],end=" ")
                print()
           
            for i in range(c1):
                perfectsum=0
                for j in range(r1):
                        num1=matrix[j][i]
                        for k in range(1,num1):
                               if num1%k==0:
                                      perfectsum=perfectsum+1
                print("number of perfect number  in column"+str(i+1)+":",perfectsum)
        case 3:
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
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                          print(matrix[i][j],end=" ")
                print()
            
            for i in range(len(matrix)):
                rowsum=0
                for j in range(len(matrix[i])):
                        rowsum=rowsum+matrix[i][j]
                print("sum of row"+str(i+1)+":",rowsum)
        case 4:
                  print("thank you visit")
                  break
                  
                
                                      

            

                            
                               
                                        
                                 
                
                          