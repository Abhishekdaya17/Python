'''70Compare the number of times 'the' and 'is' appear. S = "the cat is on the mat" the: 2, is: 1 (theis) '''
s=input("input:")
thec=0
isc=0
for i in range(0,len(s)-3+1):
    if s[i:i+3]=="the":
        thec=thec+1
for j in range(0,len(s)-2+1):
    if s[j:j+2]=="is":
        isc=isc+1
print("the:",thec,"is:",isc)