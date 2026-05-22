'''5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website'''
n = input("input: ")

str1 = n[0:3]
str2 = n[-4:]

if str1 == "www" and str2 == ".com":
    print("Valid Website")
else:
    print("Invalid Website")

