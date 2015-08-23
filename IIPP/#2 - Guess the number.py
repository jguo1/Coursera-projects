# By Jason, 2015.6.8, 271726514@qq.com
# http://www.codeskulptor.org/#user40_A6d6cfujqG_5.py (music)
# http://www.codeskulptor.org/#user40_oVrvH4scwt4XhUa.py (project)

# "Guess the number" mini-project
# It can type and range if you want

# input will come from buttons and an input field
# all output for the game will be printed in the console
import simpleguitk as simplegui
import random
import math
#count is the global variable which record the guess times
count = 0
#max is the global variable which record the max times of each game
max = 7
#range is to judge which range is currently played, True is [0,100),False is [0,1000)
range = 100
# helper function to start and restart the game
def new_game():
    range_custome()

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    range = 100
    range_custome() 

def range1000():
    # button that changes the range to [0,1000) and starts a new game  
    global range
    range = 1000
    range_custome()

def range_custome():
    global max
    global count
    global secret_number
    max = int(math.ceil(math.log(range+1,2)))
    count = 0
    secret_number = random.randrange(0,range)
    print "\n============================================="
    print "***New Game! Please input a number between 0 and "+str(range)+"***"
    print "Number of remaining guesses is "+str(max)+".\n"
    
def input_guess(guess):
    # main game logic goes here 
    print "Guess was "+guess
    global count
    count += 1
    # if count exceed max, break and start a new same range game
    if (count < max) and (int(guess) < secret_number):
        print "You have "+str(max-count)+" remaining time(s)"
        print "Higher!\n"
    elif (count < max) and (int(guess) > secret_number):
        print "You have "+str(max-count)+" remaining time(s)"
        print "Lower!\n"
    elif (count <= max) and (int(guess) == secret_number):
#        sound.play()
        print "Correct!  You get the right number by "+str(count)+" time(s)!"
        print "============================================="
        print "" 
        new_game()
    else:
        print "Sorry, you exceed the max times!"
        print "The 'secret' number is "+str(secret_number)+", try new game again!"
        print "============================================="
        print "" 
        new_game()

def input_range(custom_range):
    if float(custom_range) < 0 or (float(custom_range) != math.floor(float(custom_range))):
        print "Sorry! Please input a positive integer number!"
        return None
    global range
    range = int(float(custom_range))
    new_game()
    
# create frame
f = simplegui.create_frame("Guess the number",200,300)

# register event handlers for control elements and start frame
#f.add_button("New Game",new_game,150)
f.add_label('Choose a Range')
f.add_button("Range [0,100)",range100,200)
f.add_button("Range [0,1000)",range1000,200)
f.add_input("Enter any Range",input_range,100)
f.add_label("*Note: If you want play [0,500),type 500 in the blank above")
f.add_label("")
f.add_label("")
f.add_input("Enter a Guess",input_guess,100)
# sound = simplegui.load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg')
# call new_game 
new_game()
f.start()

# always remember to check your completed program against the grading rubric