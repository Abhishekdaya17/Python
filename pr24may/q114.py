'''114 Check if one string is a subsequence of another. S1 = "ace", S2 = "abcde" TRUE
1'''
s1 = input("S1: ")
s2 = input("S2: ")

i = 0
j = 0

while i < len(s1) and j < len(s2):

    if s1[i] == s2[j]:
        i = i + 1
        j = j + 1
    else:
        j = j + 1

if i == len(s1):
    print("TRUE")
else:
    print("FALSE")