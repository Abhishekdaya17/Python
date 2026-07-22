# Question 3: Online Shopping System
# Scenario

# An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

# Requirements

# Create a class named Product with:

# product_id
# product_name
# quantity
# price_per_item

# Initialize the values using a constructor.

# Calculations
# Total Amount = Quantity × Price Per Item
# If Total Amount > ₹5000, Discount = 10%
# Otherwise, Discount = 5%
# Final Amount = Total Amount − Discount
# Sample Input
# Enter Product ID : P101
# Enter Product Name : Laptop
# Enter Quantity : 2
# Enter Price Per Item : 35000
# Sample Output
# ------ Shopping Bill ------
# Product ID        : P101
# Product Name      : Laptop
# Quantity          : 2
# Price Per Item    : 35000.0
# Total Amount      : ₹70000.0
# Discount          : ₹7000.0
# Final Amount      : ₹63000.0
class Product:
    def __init__(self,product_id,product_name,quantity,price_per_item):
        self.product_id=product_id
        self.product_name=product_name
        self.quantity=quantity
        self.price_per_item=price_per_item
    def calcu(self):
        self.total=self.quantity*self.price_per_item
        if self.total>5000:
            self.discount=(self.total*10)/100
            self.final_amount=self.total-(self.total*10)/100
        else:
            self.discount=(self.total*5)/100
            self.final_amount=self.total-(self.total*5)/100
    def display(self):
        print(f''' ------ Shopping Bill ------
# Product ID        : {self.product_id}
# Product Name      : {self.product_name}
# Quantity          : {self.quantity}
# Price Per Item    : {self.price_per_item}
# Total Amount      : {self.total}
# Discount          : {self.discount}
# Final Amount      : {self.final_amount}''')
    
product_id=input("Enter product id:")
product_name=input("Enter product name:")
quantity=int(input("Enter product quanity:"))
price_per_item=int(input("Enter price per item:"))
obj=Product(product_id,product_name,quantity,price_per_item)
obj.calcu()
obj.display()
    
