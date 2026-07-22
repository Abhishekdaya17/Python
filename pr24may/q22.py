'''22Find the last repeating character. S = "abracadabra" r' '''
s=input("input:")


n=s
lowest=len(s)
res=""

for i in range(0,len(s)):
    ch=s[i]
    count=0
    
    for j in range(0,len(n)):
        ch1=n[j]
        if ch==ch1:
            count=count+1
            if count>=2:
                if ch not in res:
                    res=res+ch
    if count<=lowest:
        lowest=count
        
print(res)
print(res[-1])