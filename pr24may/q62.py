'''62Count vowels and consonants. S = "apple" Vowels: 2, Consonants: 3 6'''
s=input("input:")
vowel="aeiouAEIOU"
count1=0
count2=0
for i in range(0,len(s)):
    ch=s[i]
    if ch not in vowel and ch.isalpha()==True:
        count1=count1+1
    elif ch in vowel:
        count2=count2+1
    else:
        pass
print("consonants=",count1)
print("vowel=",count2)
