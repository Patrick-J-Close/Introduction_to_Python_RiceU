# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user41_KUlXzEiPlG_9.py

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
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
        self.cards = []

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s += str(self.cards[i])
        return s

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        total = 0
        ace = False
        for c in self.cards:
            total += VALUES[c.get_rank()]
 
            if c.get_rank() == "A":
                 ace = True
        
        if ace and total <= 11:
            total += 10
            
        return total
   
    def draw(self, canvas, pos):
        for c in self.cards:
            c.draw(canvas, pos)
            pos[0] += 100

            
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))                

    def shuffle(self):
        random.shuffle(self.cards) 
        pass

    def deal_card(self):
        return random.choice(self.cards)
    
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s += str(self.cards[i])
        return s 

def new_game():
    global game_deck, score
    
    score = 0
    game_deck = Deck()
    game_deck.shuffle()
    deal()
    pass

#define event handlers for buttons
def deal():
    global score, outcome, in_play, dealer_hand, player_hand
    
    if in_play:
        score -= 1
        
    dealer_hand = Hand()
    dealer_hand.add_card(game_deck.deal_card())
    dealer_hand.add_card(game_deck.deal_card())
    player_hand = Hand()
    player_hand.add_card(game_deck.deal_card())
    player_hand.add_card(game_deck.deal_card())
    in_play = True
        
    outcome = ""
    
def hit():
    global in_play, outcome, score
    
    if in_play:
        player_hand.add_card(game_deck.deal_card())
        outcome = "Hit or Stand?"
    else:
        outcome = "You need to deal again"
        return
    
    if player_hand.get_value() > 21:
        outcome = "You have busted!"
        score -= 1
        in_play = False

    
def stand():
    global in_play, outcome, score
    
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(game_deck.deal_card())
            
        if dealer_hand.get_value() > 21:
            outcome = "Dealer has busted,You win!"
            score += 1
        elif player_hand.get_value() > dealer_hand.get_value():
            outcome = "You win!"
            score += 1
        else:
            outcome = "Dealer wins, deal again?"
            score -= 1
    else:
        outcome = "You need to deal again"
    
    in_play = False

    
# draw handler    
def draw(canvas):
    global outcome, score, in_play, player_hand, dealer_hand
    
    dealer_hand.draw(canvas, [100, 200])
    player_hand.draw(canvas, [100, 400])
        
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                          [100 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]],
                         CARD_BACK_SIZE)
        
        
    canvas.draw_text("Black Jack", [50,50], 60, "Red")
    canvas.draw_text("Score: " + str(score), [400,50], 40, "Aqua")
    canvas.draw_text("Dealer Hand", [50,150], 40, "Black")
    canvas.draw_text("Player Hand", [50, 350], 40, "Black")
    canvas.draw_text(outcome, [30, 550], 50, "Yellow")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.add_button("Reset", new_game, 200)
frame.set_draw_handler(draw)


# get things rolling
new_game()
frame.start()

