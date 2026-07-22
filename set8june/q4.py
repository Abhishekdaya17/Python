# 4.
# =========================================
# FROZEN SET SUBJECT MANAGEMENT
# =========================================

# An institute offers fixed subjects:

# Python
# Java
# MySQL
# React
# Spring Boot

# These subjects cannot be modified after creation.

# Menu:
# 1. Display Subjects
# 2. Search Subject
# 3. Count Subjects
# 4. Attempt to Add Subject
# 5. Exit

# Requirements:
# - Use Frozen Set.
# - Show that modification is not allowed.
subject=frozenset(["python","java","mysql","react","react","springboot"])
while True:
    print('''# Menu:
 1. Display Subjects
 2. Search Subject
 3. Count Subjects
 4. Attempt to Add Subject
 5. Exit''')
    x=int(input("Enter the choice:"))
    match x:
        case 1:
            print(subject)
        case 2:
            s=input("enter the subject:")
            if s in subject:
                print("yes present")
            else:
                print("not present")
        case 3:
            print(len(subject))
        case 4:
            sub=input("enter the subject which you want to add:")
            subject.add(sub)
        case 5:
            print("exiting.........")
            break
        case _:
            print("invalid choice")



