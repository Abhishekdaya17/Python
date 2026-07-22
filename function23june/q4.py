# 4.
# Assignment 10: Cyber Security (Strong Password Check)

# A cybersecurity company considers a numeric password to be "strong" if every digit is even.

# Task

# Write a recursive function to check whether all digits of the given number are even.

# Input 1
# Enter Password:
# 248620
# Output 1
# Strong Password
# Input 2
# Enter Password:
# 248621
# Output 2
# Weak Password
def is_strong_password(n):
    if n == 0:
        return True

    last_digit = n % 10

    
    if last_digit % 2 != 0:
        return False

    
    return is_strong_password(n // 10)



n = int(input("Enter Password: "))

if n == 0:
    print("Weak Password")
else:
    if is_strong_password(n):
        print("Strong Password")
    else:
        print("Weak Password")