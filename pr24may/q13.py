'''13Get the Unicode code point before index. S = "Hello", Index = 1 72 (Unicode for 'H') '''
s = input("s = ")
n = int(input("index: "))

o = s[n-1]
a = ord(o)

print(a)