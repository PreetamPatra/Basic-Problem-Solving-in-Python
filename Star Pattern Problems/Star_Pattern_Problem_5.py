n=int(input("Enter a number:"))                 #Number of rows
for i in range(1,n+1):
    if i==1 or i==n:
        print("*"*n)
    else:
        for j in range(1,n+1):
            if j==1:
                print("*",end="")
            elif j==n:
                print("*")
            else:
                print(" ",end="")