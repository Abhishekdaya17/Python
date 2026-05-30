'''68Count the sum of digits present in a string. S = "a1b2c3" 6 (1+2+3) 6'''
s=input("input:")
sum=0
ns=""
for i in range(0,len(s)):
    ch=s[i]
    if ch>="1" and ch<="9":
        sum=sum+int(ch)
        ns=ns+ch+"+"
print(sum,"(",ns,"0)")