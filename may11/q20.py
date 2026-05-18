'''20) Continuous Diamond Numbers
           1
          2 3
         4 5 6
        7 8 9 10
         4 5 6
          2 3
           1'''
n =int(input("input:"))
num = 1

for i in range(1, n + 1):

    for s in range(n - i):
        print(" ", end="")

    temp = num
    for j in range(i):
        print(temp, end=" ")
        temp += 1

    num = temp
    print()

num = 4

for i in range(n - 1, 0, -1):

    for s in range(n - i):
        print(" ", end="")

    temp = num - i + 1

    for j in range(i):
        print(temp, end=" ")
        temp += 1

    print()