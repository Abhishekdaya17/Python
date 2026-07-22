'''71Print all substrings. S = "abc" "a, b, c, ab, bc, abc" 72'''
s=input("input:")
count=0
for i in range(0,len(s)):
    for j in range(i,len(s)):
        ch=s[i:j+1]
        print(ch,end=",")
        count=count+1
        print(count)


