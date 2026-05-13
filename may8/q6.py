'''6)
a
ab
abc
abcd
abcde
'''
n=int(input("enter th num:"))
i=1
while i<=n:
    print()
    ch=97
    j=1
    while j<=i:
        print(chr(ch),end="")
        ch=ch+1
        j=j+1
    i=i+1