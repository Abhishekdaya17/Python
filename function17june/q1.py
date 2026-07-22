# 1.
# STUDENT RESULT MANAGEMENT SYSTEM

# Scenario:

# A college examination department wants to automate the process of generating student results. The staff should be able to enter student details, calculate marks, determine grades, and display a complete report card using a menu-driven application.

# Develop a Python program using multiple user-defined functions and a menu-driven approach to perform the following operations.

# MENU

# 1. Add Student Details
# 2. Calculate Total Marks
# 3. Calculate Percentage
# 4. Find Grade
# 5. Display Complete Result
# 6. Find Highest Subject Mark
# 7. Find Lowest Subject Mark
# 8. Exit

# Functional Requirements

# 1. Add Student Details

#    * Student Name
#    * Roll Number
#    * Marks of 5 Subjects

# 2. Calculate Total Marks

# 3. Calculate Percentage

# 4. Find Grade

# 5. Display Complete Result

# 6. Find Highest Subject Mark

# 7. Find Lowest Subject Mark

# 8. Exit

# Grade Criteria

# Percentage        Grade

# 90 - 100          A+
# 80 - 89           A
# 70 - 79           B
# 60 - 69           C
# 50 - 59           D
# Below 50          Fail

# Constraints

# * Marks should be between 0 and 100.
# * Display an appropriate message for invalid marks.
# * The program should continue until the user chooses Exit.

# Sample Input / Output

# ******** STUDENT RESULT MANAGEMENT ********

# 1. Add Student Details
# 2. Calculate Total Marks
# 3. Calculate Percentage
# 4. Find Grade
# 5. Display Result
# 6. Find Highest Mark
# 7. Find Lowest Mark
# 8. Exit

# Enter Choice : 1

# Enter Student Name : Ajay
# Enter Roll Number : 101

# Enter Mark 1 : 78
# Enter Mark 2 : 85
# Enter Mark 3 : 92
# Enter Mark 4 : 88
# Enter Mark 5 : 77

# Student details added successfully.

# Enter Choice : 2

# Total Marks = 420

# Enter Choice : 3

# Percentage = 84.0

# Enter Choice : 4

# Grade = A

# Enter Choice : 6

# Highest Mark = 92

# Enter Choice : 7

# Lowest Mark = 77

# Enter Choice : 5

# ----------- RESULT CARD -----------

# Name        : Ajay
# Roll Number : 101

# Marks
# Subject 1 : 78
# Subject 2 : 85
# Subject 3 : 92
# Subject 4 : 88
# Subject 5 : 77

# Total Marks : 420
# Percentage  : 84.0
# Grade       : A
# Highest Mark: 92
# Lowest Mark : 77

# Enter Choice : 8

# Thank You. Program Terminated.

# Important Instructions

# 1. The solution must be developed using multiple user-defined functions.
# 2. Use appropriate parameters wherever data needs to be passed between functions.
# 3. Use return statements wherever a function needs to send a result back to the caller.
# 4. Avoid using unnecessary global variables.
# 5. Implement the application using a menu-driven approach.
# 6. Perform proper input validation.
# 7. Write meaningful function names and maintain proper code readability.

def details():

    name=input("Enter Name: ")
    rollno=int(input("Enter Roll Number: "))

    marks=[]

    for i in range(5):

        while True:

            mark=int(input(f"Enter Subject {i+1} Marks: "))

            if 0<=mark<=100:
                marks.append(mark)
                break

            else:
                print("Invalid Marks")

    return name,rollno,marks


def totalmarks(marks):
    return sum(marks)


def percentage(total):
    return (total*100)/500


def grades(per):

    if per>=90:
        return "A+"

    elif per>=80:
        return "A"

    elif per>=70:
        return "B"

    elif per>=60:
        return "C"

    elif per>=50:
        return "D"

    else:
        return "Fail"


def highest(marks):
    return max(marks)


def lowest(marks):
    return min(marks)


def showdetails(name,rollno,marks):

    total=totalmarks(marks)
    per=percentage(total)
    grade=grades(per)

    maxm=highest(marks)
    lowm=lowest(marks)

    print("\n------ RESULT CARD ------")

    print("Name =",name)
    print("Roll Number =",rollno)

    print("\nMarks")

    for i in range(5):
        print(f"Subject {i+1} =",marks[i])

    print("\nTotal Marks =",total)
    print("Percentage =",per)
    print("Grade =",grade)
    print("Highest Mark =",maxm)
    print("Lowest Mark =",lowm)


def main():

    name=""
    rollno=0
    marks=[]

    while True:

        print("""
1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit
""")

        choice=int(input("Enter Choice: "))

        match choice:

            case 1:
                name,rollno,marks=details()

            case 2:
                print("Total Marks =",totalmarks(marks))

            case 3:
                total=totalmarks(marks)
                print("Percentage =",percentage(total))

            case 4:
                total=totalmarks(marks)
                per=percentage(total)
                print("Grade =",grades(per))

            case 5:
                showdetails(name,rollno,marks)

            case 6:
                print("Highest Mark =",highest(marks))

            case 7:
                print("Lowest Mark =",lowest(marks))

            case 8:
                print("Thank You")
                break

            case _:
                print("Invalid Choice")


main()
                

            
