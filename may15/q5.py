'''5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password'''
n = input("Enter password: ")

l = len(n)

digit = 0
special = 0
space = 0

if l >= 8 and l <= 15:

    
    if n[0] >= 'A' and n[0] <= 'Z':
        uppercase = 1
    else:
        uppercase = 0

    
    if n[l-1] >= '0' and n[l-1] <= '9':
        last = 1
    else:
        last = 0

    i = 0
    while i < l:

        ch = n[i]

        
        if ch >= '0' and ch <= '9':
            digit += 1

        
        if ch in "@#$%&*":
            special = 1

        
        if ch == " ":
            space = 1

        i = i + 1

    if uppercase == 1 and last == 1 and digit >= 2 and special == 1 and space == 0:
        print("Secure Password")
    else:
        print("Invalid Password")

else:
    print("Invalid Password")
    

