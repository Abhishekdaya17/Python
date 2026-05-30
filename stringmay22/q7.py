'''
# 7. Enterprise Password Pattern Strength Analyzer

A cybersecurity company wants to validate advanced passwords.

## Conditions:

* Minimum 10 characters
* At least:

  * 1 uppercase letter
  * 1 lowercase letter
  * 1 digit
  * 1 special character
* No consecutive repeating characters
* No spaces allowed

### Input:

```text
Pyth@n1234
```

### Output:

```text
Strong Password
```

### Input:

```text
Paaass@12
```

### Output:

```text
Weak Password'''
s = input("Input: ")

upper = False
lower = False
digit = False
special = False
weak = False

# Minimum 10 characters
if len(s) >= 10:

    for i in range(len(s)):

        ch = s[i]

        
        if ch == " ":
            weak = True

    
        if ord(ch) >= 65 and ord(ch) <= 90:
            upper = True
        elif ord(ch) >= 97 and ord(ch) <= 122:
            lower = True

        # Check digit
        elif ord(ch) >= 48 and ord(ch) <= 57:
            digit = True

        # Check special character
        else:
            special = True

        # No consecutive repeating characters
        if i < len(s) - 1:
            if s[i] == s[i + 1]:
                weak = True

    if upper and lower and digit and special and not weak:
        print("Strong Password")
    else:
        print("Weak Password")

else:
    print("Weak Password")



