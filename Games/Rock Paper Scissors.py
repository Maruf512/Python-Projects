import random
list = ["Rock", "Paper", "Scissors"]
choise = random.choice(list)

def won():
    if m == 1:
        print("You have wone the ", m, "st game.")
    elif m == 2:
        print("You have wone the ", m, "nd game.")
    elif m == 3:
        print("You have wone the ", m, "rd game.")
    else:
        print("You have wone the ", m, "th game.")
    return m+1

def lose():
    if m == 1:
        print("You have lose the ", m, "st game.")
    elif m == 2:
        print("You have lose the ", m, "nd game.")
    elif m == 3:
        print("You have lose the ", m, "rd game.")
    else:
        print("You have lose the ", m, "th game.")
    return m+1

def draw():
    if m == 1:
        print("You draw the ", m, "st game.")
    elif m == 2:
        print("You draw the ", m, "nd game.")
    elif m == 3:
        print("You draw the ", m, "rd game.")
    else:
        print("You draw the ", m, "th game.")
    return m+1

sum = 0
add = 0

print(" Welcome to Rock paper scissors game. \n You will have to play 10 time's.")

m = 1
while m<10:
    print(" R for Rock. \n P for Paper. \n S for Scissor.")
    z = input("Enter: ")
    if z == "r":
        if choise == "Rock":
            print("You draw the game with the computer")
            print(draw())
            m =m+1
            x ="e"
        elif choise == "Paper":
            print("Rock has been defeated by Paper")
            print(lose())
            m =m+1
            x ="l"
        elif choise == "Scissor":
            print("Scissor has been defeated by Rock")
            print(won())
            m =m+1
            x ="w"
    elif z == "p":
        if choise == "Rock":
            print("Rock has been defeated by Paper")
            print(won())
            m =m+1
            x = "w"
        elif choise == "Paper":
            print("You draw the game with the computer")
            print(draw())
            m =m+1
            x = "e"
        elif choise == "Scissor":
            print("Paper has been defeated by Scissor.")
            print(lose())
            m =m+1
            x = "l"
    elif z == "s":
        if choise == "Rock":
            print("Scissor has been defeated by Rock")
            print(lose())
            m =m+1
            x = "l"
        elif choise == "Paper":
            print("Paper has been defeated by Scissor.")
            print(won())
            m =m+1
            x = "w"
        elif choise == "Scissor":
            print("You draw the game with the computer")
            print(draw())
            m =m+1
            x = "e"
            continue

    if x=="w":
        sum =sum+1
    elif x=="l":
        add =add+1

if sum>add:
    print("You won the game by winning ",sum," times")
elif sum<add:
    print("You lost the game by losing ",add," times")


