# 70 Compare the number of times 'the' and 'is' appear. S = "the cat is on the mat" the: 2, is: 1 (theis
s=input("enter the string==")
subs1=input("eneter the sub1:")
subs2=input("enter the subs2:")
count=0
count1=0
for i in range(0,len(s)-len(subs1)+1):
    
    if s[i:i+len(subs1)]==subs1:
        count=count+1
print(subs1,"=",count)
for i in range(0,len(s)-len(subs2)+1):
    
    if s[i:i+len(subs2)]==subs2:
        count1=count1+1
print(subs2,"=",count1)