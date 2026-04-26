'''3. Income Tax Department System

The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

* Up to ₹2,50,000 → No tax
* ₹2,50,001 to ₹5,00,000 → 5% tax
* ₹5,00,001 to ₹10,00,000 → 20% tax
* Above ₹10,00,000 → 30% tax

Write a Python program to calculate the tax amount.

Input:
Enter annual income: 800000

Output:
Tax Payable: ₹110000'''
ic=int(input("Enter Annual income"))
if ic<=250000:
	m=0
	print("no tax")
elif 250000<=ic<=500000:
	m=((ic-250000)*5)/100
	print("tax payable:",ic+m)
elif 500000<ic<=1000000:
	m=(((250000)*5)/100)+(((ic-500000)*20)/100)
	print("Tax payable:",ic+m)
else:
	m=(((250000)*5)/100)+((500000*20)/100)
	print("  Tax payable:",ic+m)
print("Net Tax:",m)
	
	