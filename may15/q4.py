'''4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11



Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U'''
n=input("input:")
count=0
count1=0
i=0
while i<len(n):
    ch=n[i]
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" \
          or ch=="U":
        count=0
    else:
        count1=count1+1
    
    
    i=i+1
print("output=",count1)    
