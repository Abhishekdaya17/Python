'''Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5'''
ms,wd,whd=map(int,input("enter monthly salary,working day and working hours per day").split(","))
sd=ms/wd
sph=sd/whd
print("Salary per day:",sd,"\n","salary per hours:",sph)