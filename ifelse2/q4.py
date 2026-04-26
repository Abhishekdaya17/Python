'''4. E-Commerce Discount Engine


An online shopping platform provides discounts to customers based on their total purchase amount:

* Above ₹5000 → 20% discount
* ₹2000 to ₹5000 → 10% discount
* Below ₹2000 → 5% discount

Write a Python program to calculate the final amount after discount.

Input:
Enter purchase amount: 4500

Output:
Final Amount: ₹4050'''
am=int(input("Enter purchase amount"))
if am>5000:
	print("Final Amount",(80*am)/100)
elif 5000>am>=2000:
	print("Final Amount",(90*am)/100)
else:
	print("final Amount",(95*am)/100)
