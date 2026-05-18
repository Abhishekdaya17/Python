'''7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number'''
n=input("input:")
alpha=0
a=0
i=0
if len(n)==10:

    while i<len(n):
        if n[:2].isalpha():
            if n[2:4].isdigit():
                a="valid"
            else:
                a="invalid"
        else:
            a="invalid"
        i=i+1
else:
    a="invalid"
print(a)