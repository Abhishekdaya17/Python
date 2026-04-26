'''14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000'''

cc=input("enter course category").lower()
ut=input("Enter user type")
if cc=="programming":
	if ut=="student":
		print("final course fee",(5000*80)/100)
	elif ut=="working professional":
		print("final course fee",(5000*90)/100)
	else:
		print("final course fee :5000")
elif cc=="design":
	if ut=="student":
		print("final course fee",(4000*80)/100)
	elif ut=="working professional":
		print("final course fee",(4000*90)/100)
	else:
		print("final course fee :4000")
else:
	if ut=="student":
		print("final course fee",(3000*80)/100)
	elif ut=="working professional":
		print("final course fee",(3000*90)/100)
	else:
		print("final course fee :3000")