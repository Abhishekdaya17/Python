'''123Convert a decimal number to binary string. N = 5 "101"'''
n = int(input("input: "))

binary = ""

while n > 0:
    rem = n % 2
    binary = str(rem) + binary
    n = n // 2

print(binary)