'''Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67
'''
tr=int(input("total runs:"))
ov=float(input("overs:"))
rb=(ov*10)%6
oo=(ov*10)//10
tb=oo*6+rb
rr=(tr/(tb/6))
print("Total balls=",tb,"\n","Run rate=",round(rr,2))
