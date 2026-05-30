'''61Count total alphabets, digits, and special characters. S = "a1b!c2" Alphabets: 3, Digits: 2, Special: 1 6'''
s=input("input:")
alphabet=0
digit=0
spc=0
for i in range(0,len(s)):
    ch=s[i]
    if ch.isalpha()==True:
        alphabet=alphabet+1
    elif ch.isdigit()==True:
        digit=digit+1
    else:
        spc=spc+1
print("alpabet=",alphabet)
print("digit=",digit)
print("spcial=",spc)


