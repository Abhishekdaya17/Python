'''6. Company Bonus Distribution System


A company wants to calculate bonuses for employees based on their years of experience:

* More than 10 years → 20% bonus
* 5 to 10 years → 10% bonus
* 2 to 5 years → 5% bonus
* Less than 2 years → No bonus

Write a Python program to calculate the bonus amount.

Input:
Enter salary: 50000
Enter years of experience: 6

Output:
Bonus Amount: ₹5000'''
sal=int(input("Enter salary:"))
ex=int(input("Enter year of experience:"))
if ex>=10:
	print("bonus amount:",(sal*20)/100)
elif 10>ex>=5:
	print("bonus ampunt:",(sal*10)/100)
elif 5>ex>=2:
	print("bonus amopunt:",(sal*5)/100)
else:
	print("no bonus:")