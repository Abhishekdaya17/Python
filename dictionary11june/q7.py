# 7.

# =========================================
# ONLINE EXAM RESULT SYSTEM
# =========================

# Store student marks in a dictionary.

# results = {
# "Ajay":88,
# "Ravi":45,
# "Neha":76,
# "Aman":39
# }

# Write a program to:

# * Display names of students who passed.
#   (Passing Marks = 50)

# Sample Output:
# Ajay
# Neha
# Ravi
results = {
    "Ajay": 88,
    "Ravi": 45,
    "Neha": 76,
    "Aman": 39
}

print("Passed Students:")

for name, marks in results.items():
    if marks >= 50:
        print(name)
