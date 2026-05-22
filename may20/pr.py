n=int(input("input:"))
for i in range(1,n+1):
        print()
        if n%2==0:
            a=n-i+1
            b=n+i-1
            for j in range(1,2*n):
                
                if j>=a and j<=b:
                    if i%2==0:
                        if j%2==1:
                            print("*",end="")
                        else:
                            print("_",end="")
                    else:
                        if j%2==0:
                            print("*",end="")
                        else:
                            print("_",end="")
                else:
                    print(" ",end="")
        else:
            
            a=n-i+1
            b=n+i-1
            for j in range(1,2*n):
                
                if j>=a and j<=b:
                    if i%2==0:
                        if j%2==1:
                            print("_",end="")
                        else:
                            print("*",end="")
                    else:
                        if j%2==0:
                            print("_",end="")
                        else:
                            print("*",end="")
                else:
                    print(" ",end="")
for i in range(n-1,0,-1):
    print()
    if n%2==0:
            a=n-i+1
            b=n+i-1
            for j in range(1,2*n):
                
                if j>=a and j<=b:
                    if i%2==0:
                        if j%2==1:
                            print("*",end="")
                        else:
                            print("_",end="")
                    else:
                        if j%2==0:
                            print("*",end="")
                        else:
                            print("_",end="")
                else:
                    print(" ",end="")
    else:
            
            a=n-i+1
            b=n+i-1
            for j in range(1,2*n):
                
                if j>=a and j<=b:
                    if i%2==0:
                        if j%2==1:
                            print("_",end="")
                        else:
                            print("*",end="")
                    else:
                        if j%2==0:
                            print("_",end="")
                        else:
                            print("*",end="")
                else:
                    print(" ",end="")

        