 

'''10. Military Recruitment Fitness System

Selection is based on age, BMI, running time, and medical condition.

If age is between 18 and 25, then check BMI. If BMI is between 18 and 25, then check running time. If running time is less than or equal to 15 minutes, then check medical. If medical is fit, select; otherwise medical reject. If running time is more than 15, physical fail. If BMI is not in range, BMI fail.

If age is between 26 and 30, then check running time and medical. If running time is less than or equal to 14 and medical is fit, conditional selection; otherwise reject.

If age is above 30 or below 18, not eligible.

Input:
 age= 23
BMI = 22
Running Time = 14
Medical = fit

Output:
Selection Status = Selected'''
age=int(input("Age="))
bmi=int(input("BMI="))
rt = int(input("running Time="))
Md=(input("Medical=")).lower()
if 25>=age>=18:
    if 25>=bmi>=18:
        if rt<=15:
            if Md=="fit":
                m="selected"
            else:
                m="rejected"
        else:
            m="physical failed"
    else:
        m="BMi failed"
elif 30>=age>=26:
    if rt<=14:
        if Md=="fit":
            m="conditional selected"
        else:
            m="rejected"
    else:
        m="rejected"
else:
    m="rejected"
print(m)

    

