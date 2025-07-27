n=int(input("Enter a number:"))                           #Number of rows
for i in range(1,n+1):
    if i%2!=0:
        print("*"*n)
    else:
        for j in range(1,n):
            if j%2==1:
                print("*",end="")
            else:
                print(" ",end="")
        if n%2==0:
            print(" ")
        else:
            print("*")