'''4. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test'''
sub=input("Subscription=").lower()
pr=int(input("Progress="))
ts=int(input("Test score"))
if sub=="premium":
    if pr>=80:
        if ts>=70:
            print("certificate")
        else:
            print("retry test")
    else:
        print("complete course")
elif sub=="basic":
    if pr>=50:
        print("limited access")
    else:
        ("locked content")
else:
    print("access denied")