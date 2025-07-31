import random
print("Welcome to SNAKE , WATER , GUN game")

cs=random.choice([-1,1,0])                          # Choice given by computer
choice={
    -1:"Water",
    1:"Snake",
    0:"Gun"
}


u=input("Enter your choice\n[\"S\" for \"Snake\" , \"W\" for \"Water\" , \"G\" for \"Gun\"]:\n")                #Choice entered by user
uchoice={
    "W":-1,
    "S":1,
    "G":0
}


if u.upper() not in ["W","S","G"]:
    print("Please select any of \"W\" or \"S\" or \"G\"")
else:
    print(f"You choosed {choice[uchoice[u.upper()]]}\nComputer choosed {choice[cs]}")
    if cs==uchoice[u.upper()]:
        print("DRAW")
    else:
        if u.upper()=="S" and cs==-1:
            print("You WON")
        elif u.upper()=="S" and cs==0:
            print("Computer WON")
        elif u.upper()=="W" and cs==1:
            print("Computer WON")
        elif u.upper()=="W" and cs==0:
            print("You WON")
        elif u.upper()=="G" and cs==-1:
            print("Computer WON")
        elif u.upper()=="G" and cs==1:
            print("You WON")

