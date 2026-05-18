'''6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number
'''
n=input("input:")
count=0
pnr=0
digit=0
if len(n)==12:
    i=0
    while i<len(n):
    
        ch=n[i]
        if n[0]=="P" and n[1]=="N" and n[2]=="R":
            pnr=1
        if ch>="0" and ch<="9":
            digit=digit+1
            
        else:
            pass
        i=i+1
    if pnr==1 and digit==9:
        print("valid pnr number")
    else:
        print("invalid pnr ")
else:
    print("invalid pnr number")
