'''11. Railway Ticket Fare System


A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600'''

ds=int(input("Enter distance:"))
clas=input("enter class:").lower()
if ds<=100:
	if clas=="sleeper":
		print("100")
	else:
		print("200")
elif 100<ds<=500:
	if clas=="sleeper":
		print("300")
	else:
		print("600")
else:
	if clas=="sleeper":
		print("500")
	else:
		print("1000")
