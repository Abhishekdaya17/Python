'''
3.
# Assignment: Prime Number Analyzer using List (Python)

## Scenario

A coaching institute stores student lucky numbers in a Python List.
Your task is to analyze the list and identify prime numbers for a scholarship selection process.

You must iterate through every element of the list and perform prime number analysis.

---

# Requirements

Write a Python program to:

1. Store integer values in a List
2. Iterate through all elements of the List
3. Check whether each number is prime or not
4. Display all prime numbers
5. Count total prime numbers
6. Count total non-prime numbers
7. Find the largest prime number from the List
8. Store all prime numbers into another List
9. Sort the prime numbers in ascending order and display them

---

# Test Case 1

## Input

[2, 3, 4, 5, 6, 7, 8]

## Expected Output

Prime Numbers: 2 3 5 7
Prime Count: 4
Non-Prime Count: 3
Largest Prime Number: 7
Prime List: [2, 3, 5, 7]
Sorted Prime List: [2, 3, 5, 7]

---

# Test Case 2

## Input

[10, 11, 12, 13, 14, 15]

## Expected Output

Prime Numbers: 11 13
Prime Count: 2
Non-Prime Count: 4
Largest Prime Number: 13
Prime List: [11, 13]
Sorted Prime List: [11, 13]

---

# Test Case 3

## Input

[1, 2, 17, 19, 20, 25]

## Expected Output

Prime Numbers: 2 17 19
Prime Count: 3
Non-Prime Count: 3
Largest Prime Number: 19
Prime List: [2, 17, 19]
Sorted Prime List: [2, 17, 19]

---

# Test Case 4

## Input

[4, 6, 8, 9, 10]

## Expected Output

Prime Numbers: None
Prime Count: 0
Non-Prime Count: 5
Largest Prime Number: Not Available
Prime List: []
Sorted Prime List: []

---

# Test Case 5

## Input

[29, 31, 37, 41]

## Expected Output

Prime Numbers: 29 31 37 41
Prime Count: 4
Non-Prime Count: 0
Largest Prime Number: 41
Prime List: [29, 31, 37, 41]
Sorted Prime List: [29, 31, 37, 41]
n=int(input("number of values:"))
a=[]
new=[]
for i in range(n):
    # str=map(str,input("enter the marks:").split())
    str=int(input("enter the number"))
    a.append(str)
print(a)
for i in range(n):
    ch=a[i]
    for j in range(2,ch-1):
        if ch%j==0 or ch==1:
            pr=pr
        else:
            pr=ch
            break
            
        new.append(pr)
print(new)'''
n = int(input("Enter total numbers: "))

a = []
prime_list = []

for i in range(n):
    num = int(input("Enter number: "))
    a.append(num)

prime_count = 0
non_prime_count = 0

for num in a:

    count = 0

    for j in range(1, num + 1):
        if num % j == 0:
            count += 1

    if count == 2:
        prime_list.append(num)
        prime_count += 1
    else:
        non_prime_count += 1

if len(prime_list) > 0:
    print("Prime Numbers:", *prime_list)
    print("Largest Prime Number:", max(prime_list))
else:
    print("Prime Numbers: None")
    print("Largest Prime Number: Not Available")

print("Prime Count:", prime_count)
print("Non-Prime Count:", non_prime_count)

print("Prime List:", prime_list)

prime_list.sort()
print("Sorted Prime List:", prime_list)
    
            



