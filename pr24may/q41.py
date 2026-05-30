'''41Check if a string contains a substring (without using contains()). S1 = "Hello", Sub = "ell" TRUE 4'''
s=input("string:")
sbs=input("substring:")
n=len(sbs)
res=False
for i in range(0,len(s)-n+1):
    if s[i:i+n]==sbs:
        res=True
        break
    
print(res)