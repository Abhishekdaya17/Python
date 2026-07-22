# 2.
# NUMBER ANALYSIS SYSTEM

# Scenario:

# A software company wants to develop a Number Analysis System. The application should be menu-driven and perform different mathematical operations on a given number.

# MENU

# 1. Check Perfect Number
# 2. Check Prime Number
# 3. Find Reverse of a Number
# 4. Calculate Factorial
# 5. Display Factors of a Number
# 6. Exit

# Requirements

# Choice 1 – Check Perfect Number

# * Accept a number from the user.
# * Pass the number to a function.
# * The function should return True if the number is Perfect, otherwise False.
# * Display an appropriate message based on the returned value.

# Choice 2 – Check Prime Number

# * Accept a number from the user.
# * Pass the number to a function.
# * The function should return a message such as "Prime Number" or "Not a Prime Number".
# * Display the returned message.

# Choice 3 – Find Reverse of a Number

# * Accept a number from the user.
# * Pass the number to a function.
# * The function should return the reversed number.
# * Display the returned value.

# Choice 4 – Calculate Factorial

# * Accept a number from the user.
# * Pass the number to a function.
# * The function should return the factorial value.
# * Display the returned value.

# Choice 5 – Display Factors of a Number

# * Accept a number from the user.
# * Pass the number to a function.
# * The function should return all factors of the given number.
# * Display the returned factors.

# Choice 6 – Exit

# Sample Output

# Enter Choice : 1

# Enter Number : 28

# 28 is a Perfect Number

# ---

# Enter Choice : 2

# Enter Number : 17

# Prime Number

# ---

# Enter Choice : 3

# Enter Number : 1234

# Reverse Number : 4321

# ---

# Enter Choice : 4

# Enter Number : 5

# Factorial : 120

# ---

# Enter Choice : 5

# Enter Number : 12

# Factors : 1 2 3 4 6 12

# ---

# Important Instructions

# 1. Create separate functions for each operation.
# 2. Use parameters to pass values to functions.
# 3. Use return statements appropriately.
# 4. Different functions should return different types of values such as Boolean, String, Integer, and Collection/List.
# 5. Avoid using global variables.
# 6. Implement the solution using a menu-driven approach.
# 7. Write meaningful function names and maintain proper code readability.
def perfect(num):
    sum=0
    for i in  range(num):
        if num%i==0:
            sum=sum+i
    if sum==num:
        print("perfect number")
    else:
        print("not perfect")
def prime(num):
    if num==1:
        print("not prime")
    else:
        flag=True
        for i in range(2,num):
            if num%i==0:
                flag=False
        if flag==True:
            print("prime")
        else:
            print("not prime")
def reversenum(num):
    reverse=0
    
    while num>1:
        digit=num%10
        reverse=reverse*10+digit
        num=num//10
    print("reverse number=",reverse)
        
def facto(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("factorial=",fact)
def dispfact(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)
def main():
    print('''# 1. Check Perfect Number
# 2. Check Prime Number
# 3. Find Reverse of a Number
# 4. Calculate Factorial
# 5. Display Factors of a Number
# 6. Exit''')
    while True:
        n=int(input("enter yout choice:"))
        match n:
            case 1:
                num=int(input("enter your number:"))
                perfect(num) 
            case 2:
                num=int(input("enter your number:"))
                prime(num)
            case 3:
                num=int(input("enter your number:"))
                reversenum(num)
            case 4:
                num=int(input("enter your number:"))
                facto(num)
            case 5:
                num=int(input("enter your number:"))
                dispfact(num)
            case 6:
                print("thank you")
                break
            case _:
                print("ivalid choice")
main()
    





