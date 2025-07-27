# Basic-Problem-Solving-in-Python
This is my first Repository
I am an NITian(NIT Rourkela) and learning basics of PYTHON

This is a program in PYTHON to check wheather the number is a prime or composite

a=int(input("Enter a number to check wether it is prime or composite:"))
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
