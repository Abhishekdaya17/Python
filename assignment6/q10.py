# '''10. Online Exam System
#     System evaluates exam conditions:

# * If marks ≥ 40 → Pass
# * If attendance ≥ 75 → Eligible for certificate

# Input:
# Enter marks: 60
# Enter attendance: 80

# Output:
# Pass
# Eligible for certificate'''
m=float(input("Enter marks:"))
a=float(input("enter attendance:"))
if m>=40:
    print("pass")
if a>=75:
    print("eligible for certificate")