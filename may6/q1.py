'''1. Utility Toolkit System

You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!

Requirements:

* Use while loop to repeat menu
* Use match-case for decision making
* Handle negative numbers properly
* Use only loops and conditions
'''
print("Menu Options:""\n"
"1 → Check Prime Number""\n"
"2 → Check Palindrome Number""\n"
"3 → Reverse a Number""\n"
"4 → Count Digits""\n"
"5 → Exit")
while True:
    x=int(input("enter the choice"))
    match x:
        case 1:
            num=int(input("enter the number"))
            if num<=1:
                print("not prime")
            else:
                i=2
                flag=True
                while i<num:
                    if num%i==0:
                        flag=False
                        break
                    i=i+1
                if flag==True:
                    print("prime")
                else:
                    print("not prime")
        case 2:
            num=int(input("Emeter the number"))
            a=num
            rev=0
            while num>0:
                rem=num%10
                rev=rev*10+rem
                num=num//10
            if a==rev:
                print("pallindrom")
            else:
                print("not pallindrome")
        case 3:
            num=int(input("Emeter the number"))
            rev=0
            while num>0:
                rem=num%10
                rev=rev*10+rem
                num=num//10
            print("reverse number is:",rev)
        case 4:
            num=input("enter the number:")
            count=0
            for i in num:
                count=count+1
            print("digit count=",count)
        case 5:
            print("exit")
            break
        case _:
            print("please enter correct number:")
                  