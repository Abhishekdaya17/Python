'''78Find the longest mirror-image substring at both ends. S = "aabccbaa" "aab" 7'''
s=input("input:")
unik=""
high=0
for i in range(0,len(s)):
    front=s[0:i+1]
    back=s[-(i+1):][::-1]
    if front==back:
        if len(front)>high:
            unik=front
            high=len(front)
    
print(unik)