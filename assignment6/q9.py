# '''9. Library Access System
#    A library checks:

# * If membership is active → Entry allowed
# * If books issued < 3 → Can issue more books

# Input:
# Membership active (yes/no): yes
# Books issued: 2

# Output:
# Entry allowed
# Can issue more books
# '''
mb=input("Menbership active(yes/no):")
bs=int(input("Book issued:"))
if mb=="yes":
    print("Entry allowed")
if mb=="no":
    print("Entry not allowed")
if bs<3:
    print("can issue more books")
if bs>=3:
    print("you cannnot issues more books")