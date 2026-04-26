'''9. Neon Number LED Unlock Game
You're programming a new LED display game. The game level unlocks only when a neon number is entered.

A neon number is a number where the sum of the digits of its square is equal to the number itself.
Example: 9 → 9² = 81 → 8 + 1 = 9

Accept a number from the player.
Check whether it is a neon number using loops.

If true, display:
Glowing Success! You've found the Neon Number!

Otherwise display:
Try again! Not quite glowing yet.

Input:
9

Output:
Glowing Success! You've found the Neon Number!'''
num=int(input("enter the num"))
num1=num**2
sum=0
i=1
while num1>0:
    rem=num1%10
    sum=sum+rem

    num1=num1//10
    


if sum==num:
    print("neon number")
else:
    print("not neon")


