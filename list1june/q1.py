'''1.
 Second Largest Unique Number
Scenario

A sports academy stores athlete scores in a list.

Find the second largest unique score.

Requirements
Read N and list elements from user
Find second largest unique number
If not available, display a message
Test Case

Input:

[10, 20, 30, 40, 40]

Output:

Second Largest = 30'''
n=int(input("size of list:"))
a=[]

for i in range(n):
        s=int(input("enter the element:"))
        a.append(s)
print(a)
unik=[]
for i in a:
    if i not in unik:
            unik.append(i)

if len(unik)>=2:
    new=[]
    new=sorted(unik)
    
    print("dusara sabse bada",new[-2])
else:
    print("no exist")
