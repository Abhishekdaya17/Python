'''53 Remove punctuation. S = "Hello, world!" "Hello world"'''
s=input("input:")
new=""
for i in range(0,len(s)):
    ch=s[i]
    if ch=="," or ch=="!" or ch=="^" or ch=="-" or ch=="_" or ch==".":
            
    
        
            new=new+""
        
    else:
        new=new+ch
print(new)