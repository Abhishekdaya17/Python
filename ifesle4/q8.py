'''8. E-Commerce Dynamic Pricing System

An e-commerce system gives discount based on demand, stock, user type, and festival.

If demand is 80 or above, then check stock. If stock is less than 50, then check user type. If user is premium, then check festival. If festival is yes, give 20% discount; otherwise 10%. If user is not premium, no discount. If stock is 50 or more, give 5% discount.

If demand is between 40 and 79, then check festival. If yes, give 10% discount; otherwise no discount.

If demand is below 40, then check stock. If stock is greater than 200, give 15% discount; otherwise no discount.

Input:
Demand = 85
Stock = 40
User Type = premium
Festival = yes

Output:
Discount = 20%'''
dem=int(input("demand="))
st=int(input("Stock="))
ut=input("User Type=")
ft=input("festival")
if dem>=80:
    if st<=50:
        if ut=="premium":
            if ft=="yes":
                m="20% discount"
            else:
                m="10% discount"
        else:
            m="no discount"
    else:
        m="5% discount"
elif 79>=dem>40:
    if ft=="yes":
        m="10% discount"
    else:
        m="no discount"
else:
    if st>=200:
        m="15% discount"
    else:
        m="no discount"
print(m)



