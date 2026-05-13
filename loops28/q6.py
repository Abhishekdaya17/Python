'''. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2
'''
num=int(input("input:"))
a=""
smallest=9
count=0
# x=0
# if num>=1:
#     print("composite")
# else:
#     while True:
#         j=2
#         while j<=num//2:
#             if num%j==0:
#                 count=count+1
#                 a="composite"
#                 break
#             j=j+1
#         else:
#             if j>num//2:
#                 count=count+0
#                 a="not composite"
#             break

#         num=num+1
# print(a)
# print(count)
count=0
for i in range(2,num+1):
    if num%i==0:
        count+=1
        if i<smallest:
            smallest =i
        
print("Count ",count+1)
print("Smallest = ",smallest)
    