'''Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code'''
n = input("Enter product code: ")

ch1 = ""
l = len(n)

for i in range(l-1, -1, -1):
    ch = n[i]
    ch1 = ch1 + ch

if ch1 == n:
    print("Palindrome Code")
else:
    print("Not a Palindrome Code")