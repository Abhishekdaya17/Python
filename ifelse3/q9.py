'''9. Multi-Level Employee Promotion System

A company promotes employees based on experience, rating, projects completed, and salary.

If experience is at least 5 years, then check rating. If rating is at least 4, then check projects. If projects are at least 3, then check salary. If salary is up to 50000, promote with 30 percent hike; otherwise 20 percent hike. If projects are less than 3, promote with 10 percent hike. If rating is below 4, no promotion. If experience is less than 5, then check if rating is 5. If yes, fast track promotion; otherwise no promotion.

Input:
Experience = 6
Rating = 4
Projects = 2

Output:
Promotion Status = Promoted with 10% hike'''

ex=int(input('Experience='))
ra=int(input('Rating='))
pj=int(input("Projects="))

if ex>=5:
    if ra>=4:
        if pj>=3:
            sal=int(input("Enter salary="))
            if sal<=50000:
                print("promted with 30% hike")
            else:
                print("promoted with 20% hike")
        else:
            print("promoted with 10% hike")
    else:
        print("no promotion")
else:
    if ra>=5:
        print("fastrack promotion")
    else:
        print("no pramotion")
