# Question 2: Electricity Bill Calculator
# Scenario


# An electricity company wants to generate monthly bills for its customers.

# Requirements

# Create a class named Customer with:

# customer_id
# customer_name
# units_consumed

# Initialize the values using a constructor.

# Calculations
# Cost per Unit = ₹8C
# Fixed Charge = ₹150
# Total Bill = (Units × 8) + 150
# Sample Input
# Enter Customer ID : C101
# Enter Customer Name : Amit Verma
# Enter Units Consumed : 350
# Sample Output
# ------ Electricity Bill ------
# Customer ID       : C101
# Customer Name     : Amit Verma
# Units Consumed    : 350
# Total Bill Amount : ₹2950.0

class customer:
    def __init__ (self,C_id,C_name,C_unit):
        self.id=C_id
        self.C_name=C_name
        self.C_unit=C_unit
        
    def calculation(self,C_unit):
        self.T_bill=(C_unit*8)+150
    def display(self):
        print(f'''
    ------ Electricity Bill ------
     Customer ID       : {self.id}
Customer Name     : {self.C_name}
Units Consumed    : {self.C_unit}
Total Bill Amount :{self.T_bill} ''')
        
C_id=input("Enter customer id:")
C_name=input("enter customer name:")
C_unit=int(input("Enter unit consumed:"))

ob=customer(C_id,C_name,C_unit)
ob.calculation(C_unit)
ob.display()


        