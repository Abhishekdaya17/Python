'''1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username'''
n=input("input:")
l=len(n)
if l>5 and l<12:
    if n[0]>="A" and n[0]<="Z" or n[0]>="a" and n[0]<="z":

        for i in range(1,l,1):
                ch=n[i]
                if ch>="1" and ch<="9" or ch>="A" and ch<="Z" or ch>="a" and ch<="z" \
                or  ch=="_":
                     a="valid user name"
                elif ch==" ":
                     a="invalid"
                     break
                else:
                     a="invalid"
                     break

    else:
         a="invalid"
else:
     a="invalid"
print(a)