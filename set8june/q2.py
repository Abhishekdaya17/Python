'''2.
=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations.'''

python=set()
java=set()
while True:
    print('''
Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit''')
    x=int(input("enter the choice:"))
    match x:
        case 1: 
            print("enter the details for python")
            n=int(input("enter the size:"))
            
            for i in range(n):
                s=int(input("name of student{n+1}:"))
                python.add(s)
        case 2:
            print("enter the details for java")
            n=int(input("enter the size:"))
            
            for i in range(n):
                s=int(input("enter the name of student{n+1}:"))
                java.add(s)
        case 3:
            print(python)
        case 4:
            print(java)
        case 5:
            print(python|java)
        case 6:
            print(python-java)
        case 7:
            print(java-python)
        case 8:
            en=input("enter the enroment=")
            if en<=python:
                print("yess")
            else:
                print("not enrolled")
        case 9:
            print(python&java)
        case 10:
            print("thank you visit again")
            break
        case _:
            print("invalid choice")
