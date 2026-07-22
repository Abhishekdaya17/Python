# QNO 1: Bank Account Management System

# ABC Bank wants to develop a software application to manage customer accounts.

# Each customer has:

# Account Number
# Customer Name
# Account Balance

# A customer should be able to:

# Deposit money
# Withdraw money
# Check account balance
# Transfer money to another customer

# The bank also wants to maintain information that is common for all customers:

# Bank Name
# Interest Rate

# The bank management may change the interest rate in the future, and the change should apply to all customers.

# Additionally, the application should provide some utility operations:

# Validate whether an account number is valid.
# Calculate interest on a given amount.
# Generate a transaction ID.
# Requirements

# Class Variables

# bank_name
# interest_rate

# Instance Variables

# account_no
# customer_name
# balance

# Instance Methods

# deposit(amount)
# withdraw(amount)
# transfer_money(receiver, amount)
# display_balance()

# Class Methods

# change_interest_rate(new_rate)
# change_bank_name(new_name)
# display_bank_info()

# Static Methods

# validate_account_number(account_no)
# calculate_interest(amount, rate)
# generate_transaction_id()

# Sample Input
# Customer 1
# Account No : 1001
# Name       : deepika
# Balance    : 50000

# Customer 2
# Account No : 1002
# Name       : Priya
# Balance    : 30000

# Deposit Amount : 10000
# Transfer Amount : 15000
# New Interest Rate : 7.5
# Sample Output
# Customer : deepika
# Balance  : 45000

# Customer : Priya
# Balance  : 45000

# Bank Name      : ABC Bank
# Interest Rate  : 7.5%
# Transaction ID : TXN1025

# Task: Design a Python class named BankAccount and implement all the above methods using instance methods, class methods, and static methods appropriately.
class BankAccount:

    
    bank_name = "ABC Bank"
    interest_rate = 5.0
    transaction_count = 1024

    
    def __init__(self, account_no, customer_name, balance):
        self.account_no = account_no
        self.customer_name = customer_name
        self.balance = balance

    
    def deposit(self, amount):
        self.balance += amount
        print("Deposit Successful")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def transfer_money(self, receiver, amount):
        if amount <= self.balance:
            self.balance -= amount
            receiver.balance += amount
            print("Transfer Successful")
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("\nCustomer :", self.customer_name)
        print("Balance  :", self.balance)


    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @classmethod
    def display_bank_info(cls):
        print("\nBank Name     :", cls.bank_name)
        print("Interest Rate :", str(cls.interest_rate) + "%")

    
    @staticmethod
    def validate_account_number(account_no):
        if len(str(account_no)) == 4:
            return True
        return False

    @staticmethod
    def calculate_interest(amount, rate):
        return (amount * rate) / 100

    @staticmethod
    def generate_transaction_id():
        BankAccount.transaction_count += 1
        return "TXN" + str(BankAccount.transaction_count)

print("Enter Customer 1 Details")
acc1 = int(input("Account Number : "))
name1 = input("Customer Name  : ")
bal1 = float(input("Balance        : "))

print("\nEnter Customer 2 Details")
acc2 = int(input("Account Number : "))
name2 = input("Customer Name  : ")
bal2 = float(input("Balance        : "))


if not BankAccount.validate_account_number(acc1):
    print("Customer 1 Account Number Invalid")
    exit()

if not BankAccount.validate_account_number(acc2):
    print("Customer 2 Account Number Invalid")
    exit()

customer1 = BankAccount(acc1, name1, bal1)
customer2 = BankAccount(acc2, name2, bal2)


deposit = float(input("\nEnter Deposit Amount : "))
customer1.deposit(deposit)

transfer = float(input("Enter Transfer Amount : "))
customer1.transfer_money(customer2, transfer)


new_rate = float(input("Enter New Interest Rate : "))
BankAccount.change_interest_rate(new_rate)


customer1.display_balance()
customer2.display_balance()

BankAccount.display_bank_info()


amount = float(input("\nEnter Amount to Calculate Interest : "))
interest = BankAccount.calculate_interest(amount, BankAccount.interest_rate)
print("Interest :", interest)


print("Transaction ID :", BankAccount.generate_transaction_id())