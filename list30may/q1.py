'''NOTE: In all programs, read the length and list elements from the user.

====================================================================

1. First Non-Repeating Number
   ====================================================================

Scenario

An online voting system stores vote IDs in a list.

Find the first vote ID that appears only once.

Requirements

* Read N and list elements from user
* Find the first non-repeating number
* If no such number exists, display an appropriate message

Test Case 1

Input:
[4, 5, 1, 2, 1, 2, 4]

Output:
First Non-Repeating Number = 5

Test Case 2

Input:
[7, 7, 8, 8]

Output:
No Non-Repeating Number Found

---'''
n=int(input("input:"))
a=[]
for i in range(n):
    str=int(input("enter the number="))
    a.append(str)


for i in a:
    count=0
    for j in a:
        if i==j:
            count=count+1
    if count==1:
        print("First non repeating number=",i)
        break
        
else:
    print("no non repeTING")
