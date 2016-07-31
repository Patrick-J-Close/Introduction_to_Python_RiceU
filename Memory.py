# http://www.codeskulptor.org/#user41_onUG0RBI9r_3.py
# Interactive Programming in Python 2, Week 5 - Memory game

# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global turns, state, cards, exposed
    turns, state = 0, 0
    cards = [i for i in range(0,8)] * 2
    random.shuffle(cards)
    exposed = [False] * 16
    pass  

# define event handlers
def mouseclick(pos):
    global state, exposed, c1, c2, cards, turns
    pick = pos[0] // 50
    
    if not exposed[pick]:
        if state == 0:
            c1 = pick
            exposed[c1] = True
            state = 1
        elif state == 1:
            c2 = pick
            exposed[c2] = True
            state = 2
            turns += 1
        elif state ==2:
            if cards[c1] != cards[c2]:
                exposed[c1], exposed[c2] = False, False
            c1 = pick
            exposed[c1] = True
            state = 1
    pass
                       
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards, exposed
    
    for c in range(len(cards)):
        if exposed[c]:
            c_pos = [50 * (c) + 12, 66]
            canvas.draw_polygon([[c*50,0],[(c+1)*50,0],[(c+1)*50,100],[c*50,100]],2,"White","Black")
            canvas.draw_text(str(cards[c]), c_pos, 50, 'White')
        else: 
            canvas.draw_polygon([[c*50,0],[(c+1)*50,0],[(c+1)*50,100],[c*50,100]],2,"Red","Green")

        label.set_text("Turns = " + str(turns))

new_game()

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
