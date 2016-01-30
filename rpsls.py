# Intro to Python course project 1: rock, paper, scissors, lizard, Spock

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
# where each value beats the two prior values and beats the two following values

import random
 
def name_to_number(name):
    # convert string input to integer value
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif  name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print("You did not enter a valid name")

    return(number)

def number_to_name(number):
    # convert integer input to string
    if number == 0:
        name = "rock"
    elif number ==1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print("a valid number was not given")

    return(name)

def rpsls(player_choice):
    # master function

    #print a blank line to seperate consecutive games
    print("")

    # print player's choice
    print("Player chooses", player_choice)

    # convert player's choice to number
    player_val = name_to_number(player_choice)

    # compute random result
    comp_val = random.randrange(0,5)

    # convert comp_val from integer to sting and print
    comp_choice = number_to_name(comp_val)
    print("Computer chooses", comp_choice)

    # determine winner
    dif = (player_val - comp_val) % 5

    if dif == 0:
        print("It's a draw!")
    elif dif == 1 or dif == 2:
        print ("Player wins!")
    elif dif == 3 or dif ==4:
        print("Compuer wins!")    

rpsls("rock")
rpsls("paper")
rpsls("scissors")
rpsls("lizard")
rpsls("Spock")

