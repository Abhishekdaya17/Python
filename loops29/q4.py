'''4.Unique Digit Security Scanner

A smart locker accepts only numbers whose all digits are unique.

Write a program using for-else loop to:

- Check every digit
- If any repeated digit found reject
- Else accept

Input:
57294

Output:
Valid Unique Code
'''
n=int(input("Enter a number: "))

while n>0:
    r=n%10
    r=str(r)
    n=n//10
    m=str(n)
    if r in m:
        print("Rejected")
        break
else :
    print("Valid Unique Code")     