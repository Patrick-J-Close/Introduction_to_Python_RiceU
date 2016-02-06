# template for "Stopwatch: The Game"
# http://www.codeskulptor.org/#user41_VEaFEfCYUUfpd18_2.py

import simplegui

# define global variables
counter = 0
nCorrect, nTotal = 0, 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    nTensSec = t%10
    nMin, t = t//600, t%600
    nSec10, t = t//100, t%100
    nSec01 = t//10
    return(str(nMin)+":"+str(nSec10)+str(nSec01)+"."+str(nTensSec))

def score():
    return(str(nCorrect) + "/" + str(nTotal))
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()

def stop_handler():
    global nTotal, nCorrect   

    if timer.is_running():
        nTotal += 1
        if counter % 10 ==0:
            nCorrect += 1
    timer.stop()

def reset_handler():
    global counter, nTotal, nCorrect
    timer.stop()
    counter, nTotal, nCorrect = 0,0,0

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(counter), [200,150], 36, "White")
    canvas.draw_text(score(), [425, 50], 28, "Green")
    
# create frame
f = simplegui.create_frame("Stopwatch Game",500,300)

# register event handlers
timer = simplegui.create_timer(100, tick)
f.add_button("Start", start_handler)
f.add_button("Stop", stop_handler)
f.add_button("Reset", reset_handler)
f.set_draw_handler(draw_handler)

# start frame
f.start()
