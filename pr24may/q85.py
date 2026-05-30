'''85 Convert string into char array.
S = "test"
Output = {'t','e','s',t}'''

s=input("input:")

arr=[]

for i in range(0,len(s)):
    arr.append(s[i])

print(arr)