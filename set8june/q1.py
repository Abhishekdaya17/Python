'''1.
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations.'''
coding=set()
robotic=set()
while True:
    print('''Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit''')
    x=int(input("enter the choice:"))
    match x:
        case 1: 
            print("enter the details for coding club")
            n=int(input("enter the size:"))
            
            for i in range(n):
                s=int(input("enter the element:"))
                coding.add(s)
        case 2:
            print("enter the details for robotics club")
            n=int(input("enter the size:"))
            
            for i in range(n):
                s=int(input("enter the element:"))
                robotic.add(s)
        case 3:
            print(coding)
        case 4:
            print(robotic)
        case 5:
            print(coding|robotic)
        case 6:
            print(coding-robotic)
        case 7:
            print(robotic-coding)
        case 8:
            print(robotic^coding)
        case 9:
            print(coding&robotic)
        case 10:
            print("thank you visit again")
            break
        case _:
            print("invalid choice")
        
        


