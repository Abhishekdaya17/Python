'''82Create a string from a character array. Char[] = {'h', 'i'} "hi"'''

s=['h','i']

new=""

for i in range(0,len(s)):
    new=new+s[i]

print(new)