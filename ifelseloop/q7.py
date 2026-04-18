'''7. A company calculates employee bonuses based on experience,
 performance rating, and salary. The system should take experience (in years), rating, and salary as input. 
If the experience is greater than or equal to 5, then check the rating. If the rating is greater than or equal to 4, then check the salary.
 If the salary is less than 50000, assign a 20% bonus; otherwise, assign a 10% bonus. If the rating is less than 4, assign a 5% bonus.
 If the experience is less than 5, no bonus is given. Display the bonus amount.

Input:
Experience = 6
Rating = 4
Salary = 40000

Output:
Bonus = 8000'''
ex=int(input("Experience:"))
ra=int(input("rating:"))
sal=int(input("salary"))
if ex>=5:
	if ra>=4:
		if sal<=40000:
			print("Bonus",(sal*20)/100)
		else:
			print("Bonus",(sal*10)/100)
	else:
		print("Bonus",(sal*5)/100)
else:
	print("no bonus")
