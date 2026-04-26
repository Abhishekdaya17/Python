'''13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600'''
sal=int(input("Enter salary"))
ra=int(input("Enter rating"))
if sal<20000:
	if ra==5:
		print("revised salary:",((sal*125)/100)+2000)
	elif ra==4:
		print("revised salary:",((sal*120)/100)+2000)
	elif ra==3:
		print("revised salary:",((sal*110)/100))
	elif ra==2:
		print("revised salary:",((sal*105)/100))
	else:
		print("no hike")
else:
	if ra==5:
		print("revised salary:",((sal*125)/100))
	elif ra==4:
		print("revised salary:",((sal*120)/100))
	elif ra==3:
		print("revised salary:",((sal*110)/100))
	elif ra==2:
		print("revised salary:",((sal*105)/100))
	else:
		print("no hike")





		

