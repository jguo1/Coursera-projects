# http://www.codeskulptor.org/#user40_BRRaZ35Oo2_0.py (test 纸牌移动版)
# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user40_Y1dZ9f2Quf_10.py

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER_BLUE = (36, 48)
CARD_BACK_CENTER_RED = (36 + 72, 48)
card_back_color = (0, 0)
times = 0

card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
prompt = ""
win = 0
lose = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit.capitalize() in SUITS) and (rank.capitalize() in RANKS):
            self.suit = suit.capitalize()
            self.rank = rank.capitalize()
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []  # create Hand object

    def __str__(self):
        hands_str = "Hand contains "
        for i in range(len(self.hand)):
            hands_str += (str(self.hand[i])+" ")
        return hands_str
    # return a string representation of a hand

    def add_card(self, card):
        return self.hand.append(card)   # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        ace = 0
        for card in self.hand:
            value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                ace +=1
        if ace > 0 and value + 10 <= 21:
            return value + 10
        else:
            return value
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.hand)):
            self.hand[i].draw(canvas,(pos[0] + i*CARD_SIZE[0],pos[1]))
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.deck.append(Card(SUITS[i],RANKS[j]))
        # create a Deck object

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        return random.shuffle(self.deck)
    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop(-1)
    def __str__(self):
        # return a string representing the deck
        deck_str = "Deck contains "
        for i in range(len(self.deck)):
            deck_str += (str(self.deck[i])+" ")
        return deck_str


#define event handlers for buttons
def deal():
    global outcome, in_play, dealer, player, deck ,win,lose, times
    outcome = ""
    times += 1
    dealer = Hand()
    player = Hand()
    deck = Deck()
    deck.shuffle()
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    if in_play == True:
        outcome = "Player lost!"
        lose += 1
    # your code goes here
        #outcome += "Player's cards "+str(player)+". And your card value is "+str(player.get_value())
    else:
        #outcome = "Player's cards "+str(player)+". And your card value is "+str(player.get_value())
        in_play = True
    
def hit():
    # replace with your code below
    global outcome, in_play, dealer, player, deck ,win,lose
    # if the hand is in play, hit the player
    if in_play == True:
        if player.get_value() <= 21:
            player.add_card(deck.deal_card())
            outcome = "Player card value is "+str(player.get_value())
            if player.get_value() > 21:
                outcome = "Player busted!"
                in_play = False
                lose += 1
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # replace with your code below
    global outcome, in_play, dealer, player, deck ,win,lose
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play == True:
        while(dealer.get_value() < 17):
            dealer.add_card(deck.deal_card()) 
        # assign a message to outcome, update in_play and score
        if dealer.get_value() > 21:
            outcome = "Dealer Busted, Player win!"
            win += 1
        else:
            if player.get_value() > dealer.get_value():
                outcome = "Player Win!  Dealer: "+str(dealer.get_value())+".Player: "+str(player.get_value())
                win += 1
            else:
                outcome = "Player lost!  Dealer: "+str(dealer.get_value())+".Player: "+str(player.get_value())
                lose += 1
        in_play = False
# draw handler    
def draw(canvas):
    global prompt,card_back_color
    # test to make sure that card.draw works, replace with your code below
    #canvas.draw_polyline([(18, 106), (598, 106), (598, 124),(18, 124),(18, 106)], 2, 'Silver')
    canvas.draw_text(outcome, (200, 180), 24, 'white', 'sans-serif')
    canvas.draw_text(prompt, (250, 430), 24, 'White', 'sans-serif')
    canvas.draw_text("BlackJack", (200, 80), 54, 'Black', 'sans-serif')
    #canvas.draw_text("Win : "+str(win)+"   Lose : "+str(lose)+"   Rounds : "+str(times), (300, 90), 22, 'Yellow', 'serif')
    canvas.draw_text("Dealer ["+str(lose)+"]", (20, 180), 24, 'White', 'sans-serif')
    canvas.draw_text("Player ["+str(win)+"]", (20, 430), 24, 'White', 'sans-serif')
    player.draw(canvas,[20,450])
    dealer.draw(canvas,[20,200])
    for i in range(len(deck.deck) - 35):
        canvas.draw_image(card_back,card_back_color,CARD_BACK_SIZE,(450 + 36- i,300 + 48 - i),CARD_BACK_SIZE)
    if in_play == True:
        prompt = "Hit or Stand?"
        canvas.draw_image(card_back,card_back_color,CARD_BACK_SIZE,(20+36,200+48),CARD_BACK_SIZE)
        if times % 2 == 0:
            card_back_color = CARD_BACK_CENTER_BLUE
        else:
            card_back_color = CARD_BACK_CENTER_RED
    else:
        prompt = "New deal?"
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric