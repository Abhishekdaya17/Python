'''2. University Result Processing System
A university wants to automatically assign grades based on marks.
Marks ≥90 → A+
Marks ≥75 → A
Marks ≥60 → B
Marks ≥50 → C
Below 50 → Fail
Write a program using a single nested inline if expression to display the grade.
'''
num=int(input("input:"))
x="A+" if num>=90 else "A" if num>=75 else "b" if num>=60 else "c" if num>=50 else "fail"
print(x)