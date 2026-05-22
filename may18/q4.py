'''4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID'''
n=input("input:")
l=len(n)
if l==8:
    if n[0]=="E" and n[1]=="M" and n[2]=="P":
        for i in range(3,l,1):
            ch=n[i]
            if ch>="0" and ch<="9":
                 a="valid employee id"
            else:
                a=" in valid"
                break
    else:
        a="invalid"
        
else:
    a="invalid"
print(a)
            
                

    
