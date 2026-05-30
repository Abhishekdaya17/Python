'''63Count frequency of each character. S = "aabcc" a: 2, b: 1, c: 2 6'''
s=input("input:")
unik=""

for i in range(0,len(s)):
    count=0
    ch=s[i]


    if ch not in unik:
        for j in range(0,len(s)):
                if ch==s[j]:
                    count=count+1
                
    
        print(ch,"=",count,end="  ")
    unik=unik+ch
