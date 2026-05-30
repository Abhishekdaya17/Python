'''79Divide a string into n equal parts. S = "abcdef", n = 3 "ab", "cd", "ef"'''
s=input("input:")
n=int(input("n="))
for i in range(0,len(s)-n+1,n):
    ch=s[i:i+n]
    print(ch,end=",")
