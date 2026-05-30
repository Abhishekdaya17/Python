'''56 Reverse only consonants. S = "apple" "eplpa"
'''
s = input("input:")
vowel = "aeiouAEIOU"

# collect consonants
cons = ""

for i in range(len(s)):
    if s[i] not in vowel:
        cons += s[i]

# reverse consonants manually (no slicing)
rev = ""
for i in range(len(cons)-1, -1, -1):
    rev += cons[i]

# rebuild string
result = ""
j = 0

for i in range(len(s)):
    if s[i] in vowel:
        result += s[i]
    else:
        result += rev[j]
        j += 1

print(result)