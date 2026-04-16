'''6. Weather Monitoring System
   A system checks weather conditions:

* If temperature ≥ 30 → Hot day
* If humidity ≥ 70 → High humidity alert

Input:
Enter temperature: 32
Enter humidity: 75

Output:
Hot day
High humidity alert'''
tem=float(input("Enter temperature:"))
hum=float(input("Enter humidity:"))
if tem>=30:
    print("Hot day")
if hum>=75:
    print("high humidity")