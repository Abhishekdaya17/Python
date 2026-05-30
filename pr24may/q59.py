'''59Rotate characters by 3 positions to the right. S = "abcde" "cdeab" 6'''
s=input("input:")
new=s[-3:]+s[:-3]
print(new)