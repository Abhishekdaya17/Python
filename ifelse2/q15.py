
'''15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220'''
vt=input("Enter vehicle type").lower()
ho=float(input("enter hours parked"))
if vt=="bike":
	print("total parking fees:",10*ho)
elif vt=="car":
	print("total parking fees",20*ho)
else:
	print("total parking fees",50*ho)