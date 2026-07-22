'''76Find the longest common suffix among strings. Strings = ["baking", "making", "taking"] "king"'''

n = int(input("Enter number of strings: "))
a = []

for i in range(n):
    s = input(f"Enter string {i+1}: ")
    a.append(s)

print(a)

# Find smallest string length
sml = len(a[0])

for i in range(1, len(a)):
    if len(a[i]) < sml:
        sml = len(a[i])

suffix = ""

for i in range(1, sml + 1):

    ch = a[0][-i]
    same = True

    for j in range(1, len(a)):
        if a[j][-i] != ch:
            same = False
            break

    if same:
        suffix = ch + suffix
    else:
        break

print("Longest Common Suffix:", suffix)