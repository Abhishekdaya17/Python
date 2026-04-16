'''Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0
'''
mrp,dp,ir,mt=map(int,input("Enter the Mobile price,Down Payment,Interest rate,Months").split())
ra=mrp-dp
twi=(10*(ra))/100+ra
mi=twi/mt
print("Remaining amount=",ra,"/n","total with interest=",twi,"/n","maonthly emi=",mi) 