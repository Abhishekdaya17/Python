'''4. Longest Consecutive Sequence
===============================

Scenario

Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 3
'''

n=int(input("input:"))
a=[]
for i in range(n):
    str=int(input("enter the number="))
    a.append(str)
new=sorted(a)
print(new)
new2=[]
maxcount=0
count=0
for i in range(0,len(new)-1):
    
    if new[i]==new[i+1]-1:
        new2.append(new[i])
        count=count+1
    else:
         count=0
    
    if count>maxcount:
            maxcount=count


    
print("longest consecutive length=",maxcount+1)
            