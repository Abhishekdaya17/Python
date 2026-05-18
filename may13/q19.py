# '''*
# * *
# *  *
# *   *
# * * * * *
# '''

# n=int(input("input:"))
# i=1
# while i<=n:
#     print()
#     if i<=2 or i==n:
#         for j in range(1,i+1,1):
#             print("*",end=" ")
#     else:
#         for k in range(1,i+1):
#             if k==1 or k==i:
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#     i=i+1
n=int(input("input:"))
i=1
while i<=n-1:
    
    for j in range(1,i+1):
        if j==1 or j==i:
         print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    i=i+1
   

for l in range(1,n+1):
      print("*",end=" ")

   