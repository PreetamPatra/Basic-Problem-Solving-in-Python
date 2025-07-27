a=int(input("Enter a number to check it is a prime or composite:"))
for m in range(2,a):
    if a%m==0:
        print(f"{a} is a composite number")
        break
else:
    if a==1:
        print("1 is neither prime nor composite number")
    elif a==2:
        print("2 is the first prime number")
    else:
        print(f"{a} is a prime number")