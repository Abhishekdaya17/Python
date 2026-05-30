'''35Find the first word that is a palindrome. S = "this madam is here" "madam" 3'''
s=input("input:")

words=s.split()

res=""



for i in range(0,len(words)):
    ch=words[i]
    if ch==ch[::-1]:
        print(ch)
    