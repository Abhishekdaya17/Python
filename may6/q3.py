'''3.

 Smart Banking System

Scenario:
You are developing a Smart Banking System for a bank to help customers perform basic banking operations such as deposit, withdrawal, balance checking, and interest calculation.

Sometimes, users may try to withdraw money or check balance before depositing any amount. Your system must handle such situations properly.

👉 Important Condition:
If no amount has been deposited yet, the system should display:
"No balance available. Please deposit first"
and should not allow withdrawal, balance check, or interest calculation.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Deposit Money
2 → Withdraw Money
3 → Check Balance
4 → Apply Interest

* Balance > 50000 → 5% interest
* Otherwise → 3% interest
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
No balance available. Please deposit first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter amount to deposit: 10000

Output:
Amount deposited successfully

---

Sample Run 3:
Input:
Enter your choice: 3

Output:
Current Balance: 10000

---

Sample Run 4:
Input:
Enter your choice: 2
Enter amount to withdraw: 15000

Output:
Insufficient balance

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Interest added: 300
Updated Balance: 10300

---

Sample Run 6:
Input:
Enter your choice: 2
Enter amount to withdraw: 5000

Output:
Withdrawal successful

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!

---
'''
print('''Menu Options:
1 → Deposit Money
2 → Withdraw Money
3 → Check Balance
4 → Apply Interest

* Balance > 50000 → 5% interest
* Otherwise → 3% interest
  5 → Exit''')
dp=0
bal=0
while True:
    x=int(input("Ener the choice:"))
    match x:
        case 1:
            dp=int(input("enter the amount of deposit:"))
            print("amount deposite succesfully")
            bal=bal+dp
            print("bal",bal)
        case 2:
            if dp==0:
                print("please deposite money first")
            else:
                wm=int(input("enter the amount withdraw"))
                if wm<=bal:
                    print("withrawal succesfull")
                else:
                    print("insuffient funds")
        case 3:
            if dp==0:
                print("please deposite money first")
            else:
                
                print("balance",bal)
        case 4:
            if dp==0:
                print("please deposite money first")
            else:
                if bal>50000:
                    ir=0.03*bal
                else:
                    ir=0.05*bal
                ttb=ir+bal


                print("interest is",ir)
                print("total balance with interest is",bal)
        case 5:
            print("exit succesfully")
            break
        case _:
            print("please enter correct value")