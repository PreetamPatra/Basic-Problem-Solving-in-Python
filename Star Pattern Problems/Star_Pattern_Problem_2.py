n=int(input("Enter a number:"))                                 #number of rows
d=1+(n-1)*2                                                     #number of dots at final row
for c in range(1,n+1):
    i=1+(c-1)*2                                                 #number of characters in any row
    print(" "*((d-i)//2)+"*"*(i)+" "*((d-i)//2))