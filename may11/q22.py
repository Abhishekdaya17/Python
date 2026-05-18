'''22) Inverted Hollow Pyramid
    *********
     *     *
      *   *
       * *
        *
'''
n = int(input("input:"))

for i in range(n):

    for s in range(i):
        print(" ", end="")

    for j in range(2 * (n - i) - 1):

        if i == 0 or j == 0 or j == 2 * (n - i) - 2:
            print("*", end="")
        else:
            print(" ", end="")

    print()