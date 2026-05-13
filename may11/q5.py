'''5) Number-Star Palindrome
    12344321
    123**321
    12****21
    1******1
'''
n=int(input("enter the number:"))
i=1
while i<=n:
    print()
    for j in range(1,(n-i)+2,1):
        print(j,end="")
    if i>=2:    
        for k in range(1,i,1):
            print("**",end="")
    for l in range((n-i)+1,0,-1):
        print(l,end="")
    i=i+1