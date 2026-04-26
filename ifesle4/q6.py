'''6. Banking Fraud Detection System

A bank checks fraud risk based on transaction amount, location, device, and transaction count.

If amount is greater than or equal to 50000, then check location. If location is international, then check device. If device is new, then check transaction count. If transactions are more than 3, mark High Risk (Block); otherwise Medium Risk. If device is not new, mark Medium Risk.

If location is domestic, then check transaction count. If more than 5, mark Medium Risk; otherwise Low Risk.

If amount is less than 50000, then check unusual activity. If yes, then check device. If device is new, mark Medium Risk; otherwise Low Risk. If no unusual activity, mark Safe.

Input:
Amount = 70000
Location = international
Device = new
Transactions = 4

Output:
Risk Level = High Risk (Blocked)
'''
am=int(input("Amount="))
lc=input("Location").lower()
dv=input("Device").lower()
tr=int(input("transaction="))
if am>=50000:
    if lc=="international":
        if dv=="new":
            if tr>=3:
                m="high risk"
            else:
                m="medium risk"
        else:
            m="medium risk"
    else:
        if tr>=5:
            m="medium risk"
        else:
            m="low risk"
else:
    ua=input("if there any unusal activity").lower()
    if ua=="yes":
        if dv=="new":
            m="medium risk"
        else:
            m="low risk"
    else:
        m="safe"
print(m)