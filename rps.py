import random
x = ["rock", "paper", "scissors"]
compp = 0
usrp = 0
gamepoint = 10
while True:
    mc = random.choice(x)
    ui = input("Rock, paper or scissors")
    if mc == ui:
        print("Computer picked " + mc)
        print("You tied")
        print("You have " + str(usrp) + " points")
        print("Computer has " + str(compp) + " points")
    elif mc == "rock" and ui == "paper":
        print("Computer picked rock")
        print("You win")
        usrp = usrp + 1
        print("You have " + str(usrp) + " points")
        print("Computer has " + str(compp) + " points")
    elif mc == "rock" and ui == "scissors":
        print("Computer picked rock")
        print("You lose")
        compp = compp + 1
        print("You have " + str(usrp) + " points")
        print("Computer has " + str(compp) + " points")
    elif mc == "paper" and ui == "rock":
        print("Computer picked paper")
        print("You lose")
        compp = compp + 1
        print("You have " + str(usrp) + " points")
        print("Computer has " + str(compp) + " points")
    elif mc == "paper" and ui == "scissors":
        print("Computer picked paper")
        print("You win")
        usrp = usrp + 1
        print("You have " + str(usrp) + " points")
        print("Computer has " + str(compp) + " points")
    elif mc == "scissors" and ui == "rock":
        print("Computer picked scissors")
        print("You win")
        usrp = usrp + 1
        print("You have " + str(usrp) + " points")
        print("Computer has " + str(compp) + " points")
    elif mc == "scissors" and ui == "paper":
        print("Computer picked scissors")
        print("You lose")
        compp = compp + 1
        print("You have " + str(usrp) + " points")
        print("Computer has " + str(compp) + " points")
    if compp > gamepoint:
        print("Computer Wins the game")
        break
    elif usrp > gamepoint:
        print("You Win the game")
        break
