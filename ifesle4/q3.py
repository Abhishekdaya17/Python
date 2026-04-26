'''3. Smart Scholarship Allocation System

A scholarship is provided based on marks, family income, and category.

If marks are 85 or above, then check income. If income is less than or equal to 300000, then check category. If category is not general, give Full Scholarship; otherwise give 75% Scholarship. If income is above 300000, give 50% Scholarship.

If marks are between 70 and 84, then check income. If income is less than or equal to 200000, give 50% Scholarship; otherwise give 25% Scholarship.

If marks are below 70, no scholarship is given.

Input:
Marks = 88
Income = 250000
Category = OBC

Output:
Scholarship = Full Scholarship'''
marks=int(input("Marks="))
inc=int(input("Income="))
cat=input("Category=").lower()
if marks>=85:
    if inc<=300000:
        if cat!="general":
            print("full scholarship")
        else:
            print("75% schoraship")
    else:
        print("50 % scholarship")
elif 70>=marks>=84:
    if inc<=2000000:
        print("50 % scholarship")
    else:
        print("25% scholarship")
else:
    print(" no scholarship")