'''67Count how many times a substring appears. S = "abab", Sub = "ab" 2 '''
s=input("input:")
sub=input("Sub=")
count=0
for i in range(0,len(s)-len(sub)+1):
    if s[i:i+len(sub)]==sub:
        count=count+1
print(count)