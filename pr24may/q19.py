'''19Find the highest frequency character. S = "abracadabra" a' '''
s=input("input:")


n=s
highest=0
res=""

for i in range(0,len(s)):
    ch=s[i]
    count=0
    
    for j in range(0,len(n)):
        ch1=n[j]
        if ch==ch1:
            count=count+1
    if count>=highest:
        highest=count
        res=ch
print(res)
        