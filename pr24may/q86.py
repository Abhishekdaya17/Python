'''86Print all permutations of a string without repetition. S = "ab" "ab", "ba"'''
s=input("input:")
sub=''
for i in range(0,len(s)):
    for j in range(0,len(s)):
        sub=s[i:j+1]
        
        
        if sub!=sub[::-1]:
            print(sub)
        
        
        
