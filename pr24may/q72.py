'''72Print all substrings of length n. S = "abc", n = 2 "ab, bc'''
s=input("input:")
n=int(input("lenght of sub string="))

for  i in range(0,len(s)-n+1):
    res=s[i:i+n]
    print(res,end=",")
