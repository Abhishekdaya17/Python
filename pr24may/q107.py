'''107 Check if a string is a pangram (contains every letter). S = "The quick brown fox jumps over the lazy dog" TRUE
'''
s=input("input:").lower()
alp=""
for i in range(len(s)):
    ch=s[i]
    if ch>="a" and ch<="z":
        if ch not in alp:
            alp=alp+ch
if len(alp)==26:
    print("pangram")
else:
    print("not")