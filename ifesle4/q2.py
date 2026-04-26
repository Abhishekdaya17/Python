'''2. Hospital Emergency Priority System

A hospital assigns treatment priority based on age, severity, and insurance.

If severity is critical, then check age. If age is 60 or above, assign Immediate ICU; otherwise assign Emergency Ward.

If severity is moderate, then check insurance. If insured, assign Priority Treatment; otherwise assign General Queue.

If severity is low, then check age. If age is less than 10, assign Pediatric Priority; otherwise assign Wait.

Input:
Age = 65
Severity = critical
Insurance = yes

Output:
Treatment = Immediate ICU
'''
age=int(input("Age="))
sv=input("severity=").lower()
ins=input("Insurance=")
if sv=="critical":
    if age>=60:
        print("immediate ICU")
    else:
        print("Emergency ward")
elif sv=="moderate":
    if ins=="insured":
        print("prirority tretment")
    else:
        print("General queue")
else:
    if age<=10:
        print("pediateric")
    else:
        print("wait")
