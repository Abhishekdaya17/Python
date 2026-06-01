'''101 Check if a string is a valid palindrome ignoring spaces and punctuation. S = "A man, a plan, a canal: Panama" TRUE
'''
s = "A man, a plan, a canal: Panama"

clean = ""


for i in s:
    if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        # convert uppercase to lowercase manually
        if i >= 'A' and i <= 'Z':
            clean = clean + chr(ord(i) + 32)
        else:
            clean = clean + i


i = 0
j = len(clean) - 1

is_pal = True

for k in range(len(clean)//2):
    if clean[i] != clean[j]:
        is_pal = False
        break
    i = i + 1
    j = j - 1

if is_pal:
    print("TRUE")
else:
    print("FALSE")