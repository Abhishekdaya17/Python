'''9. Smart Loan Eligibility System

A bank approves loans based on salary, age, credit score, and EMI.

If salary is 40000 or above, then check age. If age is between 21 and 60, then check credit score. If credit score is 750 or above, then check EMI. If EMI is less than or equal to 40% of salary, approve at 8%; otherwise approve at 10%. If credit score is below 750, then check if it is at least 650. If yes, approve at 12%; otherwise reject.

If salary is below 40000, then check if salary is at least 25000 and credit score is at least 700. If yes, approve at 13%; otherwise reject.

Input:
Salary = 50000
Age = 30
Credit Score = 760
EMI = 18000

Output:
Loan Status = Approved at 8%
'''
sal=int(input("Salary="))
ag=int(input("Age="))
emi=int(input("EMI="))
cs=int(input("Credit score="))
if sal>=40000:
        if 60>=ag>=21:
                if cs>=750:
                        if emi<=(40*sal)/100:
                                m="approved with 8 %"
                        else:
                                m="approved with 10%"
                else:
                        if cs>=650:
                                m="approved with 12%"
                        else:
                                m="reject"
        else:
                m="reject"
else:
        if sal>=25000:
                if cs>=700:
                        m="approved with 13%"
                else:
                        m="rejected"
        else:
                m="rejected"
print(m)
