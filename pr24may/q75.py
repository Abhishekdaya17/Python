'''75Find the longest common prefix among strings. Strings = ["flower", "flow", "flight"] "fl" '''

a=[]
subs=[]
s=input("enter the string:")
a.append(s)
print(a)
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            if a[i]==a[j]==a[k]:
                subs.append(a[i])
print(subs)
