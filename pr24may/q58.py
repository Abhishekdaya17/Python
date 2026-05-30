'''58Rotate characters by 2 positions to the left. S = "abcde" "cdeab" '''
s=input("input=")
new=s[2:]+s[:2]
print(new)