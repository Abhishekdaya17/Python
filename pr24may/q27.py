'''27Find the last occurrence of a word. S = "Test this test", Word = "test" 15 (index) 2'''
s = input("string:")
word = input("word:")

n = len(word)

for i in range(len(s) - n + 1):
    if s[i:i+n] == word:
        print((i+n)+1,"(index)")
        break