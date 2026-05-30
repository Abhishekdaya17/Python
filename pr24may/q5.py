'''5Compare two strings ignoring case. S1 = "Test", S2 = "test" Equal (or 0)'''

s1=input("s1=").lower()
s2=input("s2=").lower()
if s1==s2:
    print("equal")
else:
    print("not equal")