'''8. Weather Monitoring System

A weather monitoring system classifies the weather condition based on temperature:

* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.

Input:
Enter temperature: 38

Output:
Weather Condition: Hot'''
tem=int(input("Enter temperature:"))
if tem<0:
	print("freezing")
elif 0<=tem<=20:
	print("cold")
elif 21<=tem<=35:
	print("warm")
else:
	print("hot")