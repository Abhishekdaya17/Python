'''Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km'''
sp=int(input("Speed:"))
h,min=map(int,input("Enter time in hours and minute respectively").split(":"))
ttltime=round(((h*60+min*1)/60),2)
dst=60*ttltime
print("Total time:",ttltime,"\n","Distance:",dst)