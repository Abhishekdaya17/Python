# '''1. Smart Voting & ID Verification System
#    A government system verifies whether a citizen can vote and whether they have a valid ID.

# * If age ≥ 18 → Eligible to vote
# * If ID proof is available → Allowed inside booth

# Input:
# Enter age: 22
# Do you have ID (yes/no): yes

# Output:
# Eligible to vote
# Allowed inside booth
# '''
ag=int(input("Enter age:"))
x=input("Do you have ID (yes/no)")
        
if ag>=18:
    print("Eligible to vote")
if ag<18:
 print('you are not eligible to vote')
if x=="yes":
    print("Allowed inside booth")
if x=="no":    
 print("you are not allowed to go inside")    
