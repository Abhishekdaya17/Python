'''2.
Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12'''
n=input("input:")
count=0
l=len(n)
for i in range(0,l,1):
    ch=n[i]
    if ch>="0" and ch<="9":
        count=count+1
    else:
        count=count+0
print("total digits=",count)