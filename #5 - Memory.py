# http://www.codeskulptor.org/#user40_Qttfd2hKbN_7.py
# http://www.codeskulptor.org/#user40_Qttfd2hKbN_5.py
# implementation of card game - Memory

import simplegui
import random
deck = range(0,8)+range(0,8)
expose = []
temp1 = temp2 = 100
for i in range(len(deck)):
    expose.append(False)
    
card_back = simplegui.load_image('http://pic2.mofang.com.tw/2014/0731/20140731040848987.png')
card_3 = simplegui.load_image('http://img2.dwstatic.com/ls/deckbuilder/pic/Tinkmaster%20Overspark.png')
card_4 = simplegui.load_image('http://img1.dwstatic.com/ls/deckbuilder/pic/Old%20Murk-Eye.png')
card_5 = simplegui.load_image('http://img3.dwstatic.com/ls/deckbuilder/pic/Leeroy%20Jenkins.png')
card_6 = simplegui.load_image('http://img3.dwstatic.com/ls/deckbuilder/pic/Illidan%20Stormrage.png')
card_7 = simplegui.load_image('http://img4.dwstatic.com/ls/deckbuilder/pic/Baron%20Geddon.png')
card_8 = simplegui.load_image('http://img5.dwstatic.com/ls/deckbuilder/pic/Ragnaros%20the%20Firelord.png')
card_9 = simplegui.load_image('http://img4.dwstatic.com/ls/deckbuilder/pic/Nozdormu.png')
card_10 = simplegui.load_image('http://img2.dwstatic.com/ls/deckbuilder/pic/Deathwing.png')

def num_to_cardimage(n):
    if n == 0:
        return card_3
    elif n == 1:
        return card_4
    elif n == 2:
        return card_5
    elif n == 3:
        return card_6
    elif n == 4:
        return card_7
    elif n == 5:
        return card_8
    elif n == 6:
        return card_9
    elif n == 7:
        return card_10
# helper function to initialize globals
def new_game():
    global state,temp1,temp2,turn
    state = turn = 0
    temp1 = temp2 = 100
    random.shuffle(deck)
    label.set_text('Turns = 0')
    for i in range(len(deck)):
        expose[i] = False
         
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state,expose,temp1,temp2,turn
    xy = list(pos)
    # expose the cards when click
    for i in range(len(expose)):
        if xy[0] > i * 50 and xy[0] < (i+1) * 50 and expose[i] == False:
            expose[i] = True
            if state == 0:
                state = 1
                temp1 = i
            elif state == 1:
                state = 2
                temp2 = i
                turn += 1
                label.set_text('Turns = '+str(turn))
            else:
                state = 1  
                if deck[temp1] != deck[temp2]:
                    expose[temp1] = expose[temp2] = False
                temp1 = i
#            print state
#            print temp1, temp2
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for idx in range(len(deck)):
        #Draw images
        canvas.draw_image(num_to_cardimage(deck[idx]), (168 / 2, 236 / 2), (168, 236), (idx * 50 + 25, 50), (50, 100))
        #Draw text
        #canvas.draw_text(str(deck[idx]), (7 + idx * 50, 80), 80, 'white','serif')
        if expose[idx] == False:
            #Draw images card back
            canvas.draw_image(card_back, (217 / 2, 320 / 2), (217, 320), (idx * 50 + 25, 50), (50, 100))
            #Draw Green card back
            #canvas.draw_polygon([[idx * 50, 0], [(idx+1) * 50, 0],[(idx+1) * 50, 100],[idx * 50, 100]], 1, 'white', 'green')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric