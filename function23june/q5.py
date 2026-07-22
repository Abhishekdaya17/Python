# 5.
#  Hospital Record System (Search Digit)


# A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific digit exists in a patient ID.

# Task

# Write a recursive function to determine whether a given digit is present.

# Input
# Enter Patient ID:
# 5837264

# Enter Digit:
# 7
# Output
# Digit Found
# Recursive function to check if a digit exists in a number

def is_digit_present(n, digit):
    # base case: number becomes 0 and digit not found
    if n == 0:
        return False

    last_digit = n % 10

    # if digit matches
    if last_digit == digit:
        return True

    # recursive call on remaining number
    return is_digit_present(n // 10, digit)


# Input
n = int(input("Enter Patient ID: "))
digit = int(input("Enter Digit: "))

# Edge case: if ID is 0
if n == 0:
    print("Digit Found" if digit == 0 else "Digit Not Found")
else:
    if is_digit_present(n, digit):
        print("Digit Found")
    else:
        print("Digit Not Found")