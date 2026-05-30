'''66Count number of sentences in a paragraph. P = "This. Is. Test." 3'''
s=input("input:")
count=0
for i in range(0,len(s)):
    ch=s[i]
    if ch==".":
        count=count+1
print(count)