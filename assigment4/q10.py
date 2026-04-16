'''Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4
'''
s=int(input("Total seconds="))
h=s//3600
m=(s%3600)//60
sc=s-((h*3600)+m*60)
print("Hours:",h,"\n","Minutes:",m,"\n","second:",sc)