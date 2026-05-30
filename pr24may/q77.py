'''77Find the longest substring that appears at both ends. S = "abracadabra" "abra"'''
s=input("input=")
highest=""
for i in range(0,len(s)):
    for j in range(0,len(s)):
        if s[0:i]==s[-i:]:
            new=s[0:i]
            if len(new)>len(highest):
                highest=new
print(highest)