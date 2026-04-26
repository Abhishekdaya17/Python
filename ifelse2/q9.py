'''9. Student Attendance Eligibility System

A college determines whether a student is eligible to sit for exams based on attendance percentage:

* 75% and above → Eligible
* 60% to 74% → Eligible with warning
* Below 60% → Not eligible

Write a Python program to check eligibility.

Input:
Enter attendance percentage: 58

Output:
Status: Not Eligible'''
at=int(input("Enter attendance percentage:"))
if at>=75:
	print("Eligible")
elif 74>=at>=60:
	print("Eligible with warning")
else:
	print("not eligible")