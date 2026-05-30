''' 73Find the longest palindromic substring. S = "babad" "bab" (or "aba")'''
s=input("input:")
n=0

for  i in range(0,len(s)):
    for j in range(0,len(s)):
        res=s[i:j+1]
        
        if res==res[::-1]:
            if len(res)>=n:
                fres=res
                n=len(fres)
                
print(fres,end="")   

