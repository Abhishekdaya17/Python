'''23Print all characters that occur exactly twice. S = "aabbcdee" b', 'e' 2'''

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
    if count==2 and ch not in s[:i]:
            print(ch,end="")
        