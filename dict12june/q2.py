          
            

# ASSIGNMENT: ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM

# A training institute offers multiple courses such as Python, Java, Full Stack Development, Data Science, and React.

# Currently, student enrollment details are maintained manually in Excel sheets. As the number of students is increasing, the institute wants to develop a Student Management System using Python.

# The system should store student records in a nested dictionary where:

# Key → Student ID
# Value → Dictionary containing student information

# Each student record should contain:

# Student Name
# Course Name
# Mobile Number
# Fees
# City
# Sample Data Structure
# {
# 101:{
#     "name":"Ajay",
#     "course":"Python",
#     "mobile":"9876543210",
#     "fees":25000,
#     "city":"Indore"
# },
# 102:{
#     "name":"Ravi",
#     "course":"Java",
#     "mobile":"9876500000",
#     "fees":22000,
#     "city":"Bhopal"
# }
# }
# Menu Driven Program

# Display the following menu repeatedly until the user chooses Exit.

# =========================================
#  STUDENT MANAGEMENT SYSTEM
# =========================================

# 1. Add New Student
# 2. Search Student
# 3. Update Course
# 4. Delete Student
# 5. Display All Students
# 6. Count Total Students
# 7. Display Students By Course
# 8. Display Students By City
# 9. Find Student Paying Highest Fees
# 10. Find Student Paying Lowest Fees
# 11. Exit
# Functional Requirements
# 1. Add New Student

# Accept the following details:

# Student ID
# Student Name
# Course Name
# Mobile Number
# Fees
# City

# Store the information in the nested dictionary.

# Validation

# If Student ID already exists:

# Student ID Already Exists
# 2. Search Student

# Accept Student ID from the user.

# If found, display complete student information.

# Sample Output
# Student ID : 101
# Name       : Ajay
# Course     : Python
# Mobile     : 9876543210
# Fees       : 25000
# City       : Indore

# If not found:

# Student Not Found
# 3. Update Course

# Accept Student ID.

# If found:

# Ask for new course name.
# Update the course.
# Sample Output
# Course Updated Successfully
# 4. Delete Student

# Accept Student ID.

# If found:

# Delete the record.
# Sample Output
# Student Deleted Successfully

# Otherwise:

# Student Not Found
# 5. Display All Students

# Display all student records in a proper format.

# Sample Output
# -----------------------------------
# Student ID : 101
# Name       : Ajay
# Course     : Python
# Fees       : 25000
# -----------------------------------

# Student ID : 102
# Name       : Ravi
# Course     : Java
# Fees       : 22000
# -----------------------------------
# 6. Count Total Students

# Display total number of students enrolled.

# Sample Output
# Total Students : 45
# 7. Display Students By Course

# Accept a course name from the user.

# Display all students enrolled in that course.

# Sample Output
# Enter Course : Python

# 101  Ajay
# 105  Neha
# 112  Aman

# If no students are found:

# No Students Found
# 8. Display Students By City

# Accept city name from the user.

# Display all students belonging to that city.

# Sample Output
# Enter City : Indore

# 101  Ajay
# 108  Ravi
# 115  Pooja
# 9. Find Student Paying Highest Fees

# Display complete details of the student who has paid the highest fees.

# Sample Output
# Highest Fee Paying Student

# Student ID : 121
# Name       : Neha
# Course     : Data Science
# Fees       : 50000
# 10. Find Student Paying Lowest Fees

# Display complete details of the student who has paid the lowest fees.

# Sample Output
# Lowest Fee Paying Student

# Student ID : 131
# Name       : Aman
# Course     : React
# Fees       : 15000
# 11. Exit

# Terminate the application.

# Sample Output
# Thank You For Using Student Management System
d = {}

while True:
    print('''=========================================
STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit''')

    n = int(input("Enter your choice: "))

    match n:

        case 1:
            s_id = int(input("Enter Student ID: "))

            if s_id in d:
                print("Student ID Already Exists")
            else:
                name = input("Enter Name: ")
                course = input("Enter Course: ")
                mobile = input("Enter Mobile Number: ")
                fees = int(input("Enter Fees: "))
                city = input("Enter City: ")

                d[s_id] = {
                    "name": name,
                    "course": course,
                    "mobile": mobile,
                    "fees": fees,
                    "city": city
                }

                print("Student Added Successfully")

        case 2:
            s_id = int(input("Enter Student ID: "))

            if s_id in d:
                print("\nStudent ID :", s_id)
                print("Name       :", d[s_id]["name"])
                print("Course     :", d[s_id]["course"])
                print("Mobile     :", d[s_id]["mobile"])
                print("Fees       :", d[s_id]["fees"])
                print("City       :", d[s_id]["city"])
            else:
                print("Student Not Found")

        case 3:
            s_id = int(input("Enter Student ID: "))

            if s_id in d:
                d[s_id]["course"] = input("Enter New Course: ")
                print("Course Updated Successfully")
            else:
                print("Student Not Found")

        case 4:
            s_id = int(input("Enter Student ID: "))

            if s_id in d:
                d.pop(s_id)
                print("Student Deleted Successfully")
            else:
                print("Student Not Found")

        case 5:
            if d:
                for k, v in d.items():
                    print("-----------------------------------")
                    print("Student ID :", k)
                    print("Name       :", v["name"])
                    print("Course     :", v["course"])
                    print("Mobile     :", v["mobile"])
                    print("Fees       :", v["fees"])
                    print("City       :", v["city"])
            else:
                print("No Records Found")

        case 6:
            print("Total Students :", len(d))

        case 7:
            course = input("Enter Course : ")
            found = False

            for k, v in d.items():
                if v["course"].lower() == course.lower():
                    print(k, v["name"])
                    found = True

            if not found:
                print("No Students Found")

        case 8:
            city = input("Enter City : ")
            found = False

            for k, v in d.items():
                if v["city"].lower() == city.lower():
                    print(k, v["name"])
                    found = True

            if not found:
                print("No Students Found")

        case 9:
            if d:
                highest_id = None
                max_fees = -1

                for k, v in d.items():
                    if v["fees"] > max_fees:
                        max_fees = v["fees"]
                        highest_id = k

                print("\nHighest Fee Paying Student")
                print("Student ID :", highest_id)
                print("Name       :", d[highest_id]["name"])
                print("Course     :", d[highest_id]["course"])
                print("Mobile     :", d[highest_id]["mobile"])
                print("Fees       :", d[highest_id]["fees"])
                print("City       :", d[highest_id]["city"])
            else:
                print("No Data")

        case 10:
            if d:
                lowest_id = None
                min_fees = 999999999

                for k, v in d.items():
                    if v["fees"] < min_fees:
                        min_fees = v["fees"]
                        lowest_id = k

                print("\nLowest Fee Paying Student")
                print("Student ID :", lowest_id)
                print("Name       :", d[lowest_id]["name"])
                print("Course     :", d[lowest_id]["course"])
                print("Mobile     :", d[lowest_id]["mobile"])
                print("Fees       :", d[lowest_id]["fees"])
                print("City       :", d[lowest_id]["city"])
            else:
                print("No Data")

        case 11:
            print("Thank You For Using Student Management System")
            break

        case _:
            print("Invalid Choice")
                        
