# Rock-paper-scissors-lizard-Spock


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def name_to_number(name):
    if (name == 'rock') or (name == 'Rock'):
        name = 0
        return name
    elif (name == 'Spock') or (name == 'spock'):
        name = 1
        return name
    elif (name == 'paper') or (name == 'Paper'):
        name = 2
        return name
    elif (name == 'lizard') or (name == 'Lizard'):
        name = 3
        return name 
    elif (name == 'scissors') or (name == 'Scissors'):
        name = 4
        return name
    else:
        print "Invalid Name Selection"


def number_to_name(number):
    if number == 0:
        number = 'rock'
        return number
    elif number == 1:
        number = 'Spock'
        return number
    elif number == 2:
        number = 'paper'
        return number
    elif number == 3:
        number = 'lizard'
        return number
    elif number == 4:
        number = 'scissors'
        return number
    else:
        print "Invalid Number Selection"
    

def rpsls(player_choice): 
    playerNumb = name_to_number(player_choice)
    randomChoice = random.randint(0, 4)
    computerChoice = number_to_name(randomChoice)
    print ""
    print "Player chooses", player_choice
    print "Computer chooses", computerChoice
    diff = randomChoice - playerNumb
    if (diff < 0):
        diff = diff +5
    if (diff == 1) or (diff == 2):
        print "Computer Wins!"
    elif (diff == 3) or (diff == 4):
        print "Player Wins!"
    elif diff == 0:
        print "Player and Computer tie!"
    else:
        print "Something is wrong in Determing who wins"
        
        

 
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


