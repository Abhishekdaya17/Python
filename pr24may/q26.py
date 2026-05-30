'''26Find the first occurrence of a word. S = "Test this test", Word = "test" 10 (index) '''
s = input("string:")
word = input("word:")

n = len(word)

for i in range(len(s) - n + 1):
    if s[i:i+n] == word:
        print(i)
        break