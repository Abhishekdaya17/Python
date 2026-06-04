'''3.

=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
153 121 10
370 22 44
407 15 131

Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1

---------------------------------------------------------

Enter your choice: 2

Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2

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
    print('''Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit 
    
        ''')
   
        
    n=int(input("enter the choice:"))
    match n:
            case 1:
                for i in range(len(matrix)):
                    count=0
                    for j in range(len(matrix[i])):
                            ch=str(matrix[i][j])
                            sum=0
                            for k in ch:
                                sum=sum+int(k)**len(ch)
                            if sum==int(ch):
                                count=count+1
                    print("Row"+str(i)+"Armstrong Count =",count)
            
                        


            case 2:   
                for i in range(len(matrix)):
                        count=0
                        for j in range(len(matrix[i])):
                            ch=str(matrix[j][i])
                            if ch==ch[::-1]:
                                count=count+1
                        print("coulmn"+str(i+1)+"pallindrome count:",count)
            case 3:
                for i in range(len(matrix)):
                    sum=0
                    for j in range(len(matrix[i])):
                            sum=sum+matrix[i][j]
                    print("average of  row"+str(i)+":",sum/len(matrix[i]))
            case 4:
                print("Thank You for Using Matrix Quality Check System")
                break
            case _:
                print("invalid choice")

                    
            
