'''37Reverse each word in a string. S = "cat dog" "tac god" 3'''
s=input("input:")
word=s.split()
for i in range(0,len(word)):
    ch=word[i]
    res=ch[::-1]
    print(res,end=" ")