'''54 Replace duplicate chars with '$'. S = "hello" "he$lo"
'''
'''54 Replace duplicate chars with '$'. S = "hello" -> "he$lo"'''

s = input("input: ")

new = ""

for i in range(0, len(s)):
    ch = s[i]
    count = 0

    for j in range(0, i):
        if ch == s[j]:
            count = count + 1

    if count > 0:
        new = new + "$"
    else:
        new = new + ch

print(new)