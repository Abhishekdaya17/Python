'''6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching'''
n1=input("input:").lower()
n2=input("input:").lower()
str1=""
str2=""
l=len(n1)
l2=len(n2)
for i in range(0,l):
    ch=n1[i]
    if ch!=" ":
        str1=str1+ch
for i in range(0,l2):
    ch1=n2[i]
    if ch1!=" ":
        str2=str2+ch1
if sorted(str1)==sorted(str2):
    print("both codes are matching")
else:
    print("not matching")

