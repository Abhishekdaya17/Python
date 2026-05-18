'''17) Hollow Hourglass
    * * * * *
      *     *
        * *
          *
        * *
      *     *
    * * * * *'''
n =int(input("input:"))

for i in range(n):

    for s in range(i):
        print(" ", end=" ")

    for j in range(n - i):
        if j == 0 or j == n - i - 1 or i == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

for i in range(n - 2, -1, -1):

    for s in range(i):
        print(" ", end=" ")

    for j in range(n - i):
        if j == 0 or j == n - i - 1 or i == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()