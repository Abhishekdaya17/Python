'''
18) Binary Floyd Triangle
    1
    0 1
    1 0 1
    0 1 0 1

'''
n =int(input("input:"))
num = 1

for i in range(1, n + 1):

    for j in range(i):
        print(num % 2, end=" ")
        num += 1

    print()