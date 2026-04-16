#Assignment 1: Time Converter
#========================================
#An event management company is developing a scheduling system. One of the key tasks is converting the duration of events from total seconds (which their sensor system records) into a more human-readable format of hours, minutes, and seconds.
#Write a Python program that:
#- Accepts the total event duration in seconds as input.
#- Calculates how many hours, minutes, and seconds it corresponds to.
#- Displays the output in the format:
#  Hours: x, Minutes: y, Seconds: z

#Sample Input:
#Total event duration in seconds: 3672

#Sample Output:
#Hours: 1, Minutes: 1, Seconds: 12

a=int(input("total event duration in second:"))
hours=a//3600

minute=a//60

min=minute-(hours*60)
second=a-(hours*3600+min*60)
print("hours:",hours,"minute:",min,"second:",second,sep="  ")