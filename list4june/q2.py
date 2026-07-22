'''2.
Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")'''
n=int(input("size of array:"))

a=[]
for i in range(0,n):
    valu=input("Enter the value"+str(i+1)+":")
    a.append(valu)
print(a)
count=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        flag=True
        for k in range(len(a[j])):
            if a[j][k] in a[i]:
                print(a[j][k])
                flag=False
                break
            
        if flag==True:
            count=count+1
print(count)

                 