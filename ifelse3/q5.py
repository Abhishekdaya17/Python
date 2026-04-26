'''5. Smart Warehouse Dispatch System

A warehouse decides dispatch strategy based on stock availability, priority level, and delivery distance.

If stock is at least 100, then check priority. If high priority, then check distance. If distance is up to 200, dispatch immediately; otherwise use fast courier. If priority is not high, then check if stock is at least 300. If yes, bulk dispatch; otherwise normal dispatch. If stock is less than 100, then check if stock is at least 50. If yes, and priority is high, partially dispatch; otherwise hold. If stock is below 50, mark out of stock.

Input:
Stock = 120
Priority = high
Distance = 300

Output:
Dispatch Status = Dispatch via Fast Courier'''
st=int(input("Stock="))
pr=input("priority=").lower()
ds=int(input("enter distance="))
if st>=100:
    if pr=="high":
        if ds<=200:
            print("dispatched immediately")
        else:
            print("Dispatch  via fast courier")
    else:
        if ds>=300:
            print("Bulk dispatch")
        else:
            print("normal dispatched")
else:
    if st>=50:
        if pr=="high":
            print("partially dispatch")
        else:
            print("hold")
    else:
        print("hold")
    