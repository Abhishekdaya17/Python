'''12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680'''
am=int(input("Enter bill amount:"))
if am<1000:
	print("Fill Bill Amount:",(105*am)/100)
elif 1000<am<=5000:
	if am>3000:
		print("Final bill Amount",(((112*am)/100)+200))
	else:
		print("Final bill Amount",(112*am)/100)
else:
	print("final bill amount",((118*am)/100)+200)

