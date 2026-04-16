'''/you are developing a feature for a health and wellness mobile app that helps users understand how long they've been alive in a more tangible way.

Write a Python program that:
- Accepts the user’s age in years as input.
- Calculates the approximate number of:
  Days lived (1 year = 365 days)
  Hours lived
  Minutes lived
- Displays the output in the format:

You've lived approximately:
Days: xxx
Hours: yyy
Minutes: zzz

Sample Input:
Enter your age in years: 18

Sample Output:
You've lived approximately:
Days: 6570
Hours: 157680
Minutes: 9460800
'''
import math
age=int(input("Enter your age in year:"))
dy=age*365
hr=dy*24
mn=hr*60
print("you have lived approximately","\n","days:",dy,"\n","hours:",hr,"\n","minutes:",mn)
