'''55 Reverse only vowels. S = "hello" "holle"'''
s = input("input:")

vowels = "aeiouAEIOU"

# collect vowels first
vowel_list = ""

for i in range(len(s)):
    if s[i] in vowels:
        vowel_list += s[i]

# now rebuild string with reversed vowel usage
result = ""
index = len(vowel_list) - 1

for i in range(len(s)):
    if s[i] in vowels:
        result += vowel_list[index]
        index -= 1
    else:
        result += s[i]

print(result)