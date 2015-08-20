# http://www.codeskulptor.org/#user40_WBEyLSKo5G_3.py
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    """ Converts the string name into a number between 0 and 4 as described above"""
    if name.lower() == "rock":
        return 0
    elif name.lower() == "spock":
        return 1
    elif name.lower() == "paper":
        return 2
    elif name.lower() == "lizard":
        return 3
    elif name.lower() == "scissors":
        return 4
    else:
        return -1

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    """Converts a number in the range 0 to 4 into its corresponding name as a string"""
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    else:
        return "scissors"

    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
import random

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    """ Rock-paper-scissors-lizard-Spock game!"""
    
    # print a blank line to separate consecutive games
    print ""
    # print out the message for the player's choice
    print "Player chooses "+player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses "+comp_choice
    # compute difference of comp_number and player_number modulo five
    if player_number == -1:
        print "Whoops! Wrong input confused computer, please try again"
    else:
        result = (player_number - comp_number) % 5
        # use if/elif/else to determine winner, print winner message
        if result == 1 or result == 2:
            print "Player wins!"
        elif result == 3 or result == 4:
            print "Computer wins!"
        elif result == 0 :
            print "Player and computer tie!"
        else:
            print "Must be incorrect in some place"
            
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


