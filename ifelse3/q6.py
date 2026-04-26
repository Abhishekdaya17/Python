'''6. Banking Fraud Detection System

A bank monitors transactions based on amount, location, OTP verification, and account age.

If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.

Input:
Transaction Amount = 60000
Location = domestic
Account Age = 1

Output:
Transaction Status = Flagged
'''
tr=int(input("Transaction amount="))
lc=input("Location=")
aa=float(input("Account age="))
ua=input("Unsual activity answer it in yes or no:")
if tr>=10000:
    if lc=="international":
        otp=int(input("Enter otp:"))
        if otp==1234:
            print("allowed")
        else:
            print("wrong otp")
    elif lc=="domestic":
        if tr>=50000:
            if aa>=2:
                 print("allowed")
            else:
                print("Flag")
        else:
            print("allow")
else:
    if ua=="yes":
        print("flag")
    else:
        print("allow")
