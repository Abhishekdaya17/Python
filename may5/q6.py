'''6.
Data Validation System – Character Identifier
A system needs to validate user input characters.
If the input is:
Alphabet → display "Alphabet"
Digit → display "Digit"
Otherwise → display "Special Character"
Write a program using inline if to classify the character.'''

'''print(ord("A"))
print(ord("Z"))
print(ord("a"))
print(ord("z"))
print(ord("0"))
print(ord("9"))'''
x=input("input:")
for i in x:
    p=ord(i)
    n="Alphabet" if p>=65 and p<=90 or p>=97 and p<=122 else "digit" if p>=48 and p<=57 else "special char"
    
    print(n)

    