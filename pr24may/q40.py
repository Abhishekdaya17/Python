'''40Search all occurrences of a word. S = "a b a b", Word = "b" 2, 6 (start indices) 4'''
s=input("input")
word = input("word:")

n = len(word)

for i in range(len(s) - n + 1):
    if s[i:i+n] == word:
        print(i,end=" ")
        