'''2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17

'''
x=int(input("input"))
i=x+1
sum=0
if x<=1:
    print("3")
else:
    while True:
        j=2
        while j<=i//2:
            if i%j==0:
                break
            j=j+1
        if j>i//2:
            print(i)
            break
        i=i+1


