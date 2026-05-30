'''84 Print ASCII value of each character.
S = "A"
Output:
A : 65
'''

s=input("input:")

for i in range(0,len(s)):
    print(s[i],":",ord(s[i]))