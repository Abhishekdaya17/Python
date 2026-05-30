'''69Count how many times 'life' appears in a string. S = "life is life" 2 7'''
s=input("input:")
count=0
for i in range(0,len(s)-4+1):
    if s[i:i+4]=="life":
        count=count+1
print(count)