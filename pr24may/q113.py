''''''s = input("input: ")

n = len(s)
max_len = 0

for i in range(1 << n):

    sub = ""

    for j in range(n):
        if (i >> j) & 1:
            sub = sub + s[j]

    # palindrome check (manual)
    is_pal = True
    left = 0
    right = len(sub) - 1

    while left < right:
        if sub[left] != sub[right]:
            is_pal = False
            break
        left = left + 1
        right = right - 1

    if is_pal:
        if len(sub) > max_len:
            max_len = len(sub)

print(n - max_len)