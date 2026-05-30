'''32Count the frequency of each word. S = "apple banana apple" apple: 2, banana: 1 '''
s=input("input:")

words=s.split()


printed=[]
for i in range(0,len(words)):
    ch=words[i]
    if ch not in printed:
        count=0
        for j in range(0,len(words)):
            ch1=words[j]
            if ch==ch1:
              count=count+1
        print(ch,count,end=" ")
        printed.append(ch)
