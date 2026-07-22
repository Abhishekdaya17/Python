'''7.

A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
361

Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)'''
n = int(input("Enter number of products: "))
products = []
for i in range(n):
    print(f"\nEnter Product {i+1} details:")
    product_id = input("Enter Product ID: ")
    product_name = input("Enter Product Name: ")
    price = int(input("Enter Price: "))
    products.append((product_id, product_name, price))

print("\nAll Products:")
for p in products:
    print(p)

costliest = products[0]
cheapest = products[0]
total_price = 0
for p in products:
    if p[2] > costliest[2]:
        costliest = p
    if p[2] < cheapest[2]:
        cheapest = p
    total_price += p[2]

print("\nCostliest Product:")
print(costliest)

print("\nCheapest Product:")
print(cheapest)

print("\nAverage Price:")
print(total_price / n)

print("\nProducts Above ₹50,000:")
for p in products:
    if p[2] > 50000:
        print(p)