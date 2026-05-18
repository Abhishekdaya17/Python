'''''5) Zig-Zag Star
    *   *   *
      *   *
    *   *   *'''
n=int(input("input:"))
for i in range(n):

    for j in range(n*n):

        if (i == 0 and j % 4 == 0) or \
           (i == 1 and j % 4 == 2) or \
           (i == 2 and j % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")

    print()