'''16) Palindrome Pyramid
            1
           121
          12321
         1234321
        123454321'''
n = int(input("input:"))

for i in range(1, n + 1):

    for s in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()