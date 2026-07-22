'''3.
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.



Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operations.'''

visitor=set()
while True:
    print('''
        Menu:
        1. Add Visitor
        2. Remove Visitor
        3. Check Visitor
        4. Display All Visitors
        5. Count Unique Visitors
        6. Clear Visitor Data
        7. Exit''')

    x=int(input("enter the choice:"))
    match x:
        case 1: 
            print("enter the details for visitor")
            n=int(input("enter the size:"))
            
            for i in range(n):
                s=int(input("enter the id of visitor{n+1}:"))
                visitor.add(s)
        case 2:
            en=input("enter the id=")
            if en<=visitor:
                print("yess")
            else:
                print("not enrolled")
        case 3:
            
            
                s=int(input("enter the id  of visitor{n+1}:"))
                visitor.remove(s)
        
        case 4:
            print(visitor)
        case 5:
            print(len(visitor))
        case 6:
            visitor.clear()
        case 7:
            print("Exiting...........")
            break
       
        case _:
            print("invalid choice")
