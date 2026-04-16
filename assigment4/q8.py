'''Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0
'''
import math
p,r,t=map(int,input("enter the principal,rate and time respectively:").split(","))
a=(p*(((r/100)+1)**t))


print("amount after interest:",a)