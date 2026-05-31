'''8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found

---'''

# n=int(input("input:"))
# a=[]
# for i in range(n):
#     str=int(input("enter the number="))
#     a.append(str)

# max=0
# maj=[]
# for i in a:
#     count=0
#     for j in a:
#         if i==j:
#             count=count+1
#             if count>max:
#                 max=count
#                 maj=i
   
        
        
        
# else:
#     print("no repeating number")
# print("majority=",maj)
n = int(input("input: "))
a = []

for i in range(n):
    num = int(input("enter number: "))
    a.append(num)

majority = -1

for i in a:
    count = 0

    for j in a:
        if i == j:
            count += 1

    if count > n // 2:
        majority = i
        break

if majority == -1:
    print("No Majority Element Found")
else:
    print("Majority Element =", majority)

    

