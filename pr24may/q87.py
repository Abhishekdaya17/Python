'''87 Print all permutations of a string with repetition. S = "aab" "aab", "aba", "baa"'''
s = input("Enter string: ")
new=[]

for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):

            if i != j and j != k and i != k:

                p = s[i] + s[j] + s[k]
                if p not in new:
                    new.append(p)
print(" ".join(new))
