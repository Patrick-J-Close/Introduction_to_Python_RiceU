# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui, random, math

# initialize global variables
high = 100
low = 0
attempts = 0
attempt_limit = math.ceil(math.log(high-low,2))
secret_number = 0

# helper function to start and restart the game
def new_game():
    
    print("Welcome!\n")
    range100()

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    global high, low, attempts, attempt_limit, secret_number
    high = 100
    attempts = 0 
    attempt_limit = math.ceil(math.log(high-low,2))
    secret_number = random.randrange(low, high)
    
    print("You have started a new game in the range [0, 100)")
    print("You have " + str(attempt_limit - attempts)+ " attempts remaining\n")

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    global high, low, attempts, attempt_limit, secret_number
    high = 1000
    attempts = 0
    attempt_limit = math.ceil(math.log(high-low,2))
    secret_number = random.randrange(low, high)
    
    print("You have started a new game in the range [0, 1000)")
    print("You have " + str(attempt_limit - attempts)+ " attempts remaining\n")

def attempt_suffix(attempt):
    """Adds suffix to attempt number"""
    
    if attempt == 1:
        suffix = "st"
    elif attempt == 2:
        suffix = "nd"
    elif attempt == 3:
        suffix = "rd"
    else:
        suffix = "th"
    return(suffix)
        
def input_guess(guess):
    
    global high, low, attempts, attempt_limit, secret_number

    # increment attempts for a non-blank input
    if guess != "" and int(guess) < int(high):
        guess = int(guess) 
        secret_number = int(secret_number)
        attempts += 1
        
        print("Your " + str(attempts) + attempt_suffix(attempts) +
              " guess was: " + str(guess))
        if guess < secret_number:
            print("Go higher!")
            print("You have " + str(attempt_limit - attempts) + 
                  " guesses remaining")
        elif guess > secret_number:
            print("Go lower!") 
            print("You have " + str(attempt_limit - attempts) +
                  " guesses remaining")
        else:
            print("You are correct!\n")
        if attempts == attempt_limit:
            print("You are out of guesses")
            print("Game Over\n")
        else:
            print("")
    else:
        print("You did not enter a value, try again\n")
                            
# create frame
f = simplegui.create_frame("Guess the Number", 400, 300)

# register event handlers for control elements and start frame
f.add_label("Select a range for a new game:")
f.add_label("")
f.add_button("Range [0,100)", range100, 200)
f.add_button("Range [0,1000)", range1000, 200)
f.add_label("")
f.add_input("Enter your guess:", input_guess, 200)

# call new_game  
new_game()

# start frame
f.start()
