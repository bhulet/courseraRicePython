# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num_range = 100
counter = 7

# helper function to start and restart the game
def new_game():
    global secret_number
    global num_range
    global counter
    secret_number = random.randrange(0, num_range)
    if (num_range == 100):
        counter = 7
    else:
        counter = 10
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is", counter
    print ""

# define event handlers for control panel
def range100():
    global counter
    global num_range
    counter = 7
    num_range = 100
    new_game()



def range1000():
    global num_range
    global counter
    num_range = 1000
    counter = 10
    new_game()
    
    
def input_guess(guess):
    global counter
    global num_range
    global secret_number
    guess = int(guess)
    print "Guess was", guess
    if (guess > num_range - 1) or (guess < 0):
        print "Your guess is outside the range for this game"
        print "Number of remaining guesses is", counter 
        print ""
    elif (guess > secret_number):
        counter = counter - 1
        if (counter == 0):
            print "You lose. The secret number was", secret_number
            print ""
            new_game()        
        else:
            print "Lower!"
            print "Number of remaining guesses is", counter
            print ""
    elif (guess < secret_number):
        counter = counter - 1
        if (counter == 0):
            print "You lose. The secret number was", secret_number
            print ""
            new_game()        
        else:
            print "Higher!"
            print "Number of remaining guesses is", counter
            print ""
    elif (guess == secret_number):
        print "Correct!"
        print ""
        new_game()
    else:
        print "Something went wrong in input guess"
        print ""

    
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)


# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a Guess", input_guess, 200)

# call new_game 
new_game()


