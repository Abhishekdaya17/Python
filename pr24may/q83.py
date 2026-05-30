'''83 Create a string from a byte array.
Byte[] = {72,101,108}
Output = "Hel"
'''

s=[72,101,108]

new=""

for i in range(0,len(s)):
    new=new+chr(s[i])

print(new)