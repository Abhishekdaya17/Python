'''39Search all occurrences of a character. S = "banana", Char = 'a' 1, 3, 5 (indices) 4'''
s=input("input:")
w=input("char=")
for i in range(0,len(s)):
    ch=s[i]
    if ch==w:
        print(i,"(indices)",end=" ")