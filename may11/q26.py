'''27) Continuous Number Pyramid
            1
           2 3
          4 5 6
         7 8 9 10'''
n = int(input("input:"))

for i in range(n, 0, -1):

    for s in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()

for i in range(2, n + 1):

    for s in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()