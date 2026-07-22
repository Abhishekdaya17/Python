'''75Find the longest common prefix among strings. Strings = ["flower", "flow", "flight"] "fl" '''
n = int(input("Enter the number of strings: "))
a = []

for i in range(n):
    s = input(f"Enter string {i+1}: ")
    a.append(s)

print(a)

# Find length of smallest string
sml = len(a[0])

for i in range(1, len(a)):
    if len(a[i]) < sml:
        sml = len(a[i])

prefix = ""

for i in range(sml):
    ch = a[0][i]
    same = True

    for j in range(1, len(a)):
        if a[j][i] != ch:
            same = False
            break

    if same:
        prefix += ch
    else:
        break

print("Longest Common Prefix:", prefix)
    
