# Implementation of classic arcade game Pong
# http://www.codeskulptor.org/#user41_FnyDHdDVN0no3qg.py

#import simpleguitk as simplegui
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_vel = paddle2_vel = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    vel_x = random.randrange(120,240) / 60
    vel_y = random.randrange(60,180) / 60
    
    d = random.randrange(0,2)
    if d == 1: 
        vel_y = -vel_y
    if direction == "RIGHT":
        ball_vel = [vel_x,vel_y]
    else:
        ball_vel = [-vel_x,vel_y]    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    score1 = score2 = 0
    paddle1_pos = paddle2_pos = HEIGHT / 2
    
    d = random.randrange(0,2)
    if d == 1:
        spawn_ball("RIGHT")
    else:
        spawn_ball("LEFT")

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
   
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # detect collision with top or bottom wall and deflect
    if(ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS) or (ball_pos[1] <= BALL_RADIUS - 1):
        ball_vel[1] = - ball_vel[1]
    
    # detect collision with paddle and deflect OR update score and spawn new game
    if(ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS):
        if(ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT):
            # collision with right paddle
            ball_vel[0] = -(ball_vel[0] * 1.1)
        else: 
            score1 += 1
            spawn_ball("LEFT")
    if(ball_pos[0] <= 0 + PAD_WIDTH + BALL_RADIUS):
        if(ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT):
            # collision with left paddle
            ball_vel[0] = -(ball_vel[0] * 1.1)
        else: 
            score2 += 1
            spawn_ball("RIGHT")        
            
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2,"White","White")
    
    # draw paddles
    canvas.draw_polygon([[0,paddle1_pos - HALF_PAD_HEIGHT], 
               [PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], 
               [PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT],
               [0, paddle1_pos + HALF_PAD_HEIGHT]], 2, "White", "White")
    canvas.draw_polygon([[WIDTH, paddle2_pos - HALF_PAD_HEIGHT], 
               [WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], 
               [WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT],
               [WIDTH, paddle2_pos + HALF_PAD_HEIGHT]], 2, "White", "White")  
    
    # update paddles and keep on canvas
    paddle1_pos += paddle1_vel
    if(paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT  
    elif(paddle1_pos <= HALF_PAD_HEIGHT):
        paddle1_pos = HALF_PAD_HEIGHT
        
    paddle2_pos += paddle2_vel
    if(paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT  
    elif(paddle2_pos <= HALF_PAD_HEIGHT):
        paddle2_pos = HALF_PAD_HEIGHT
    
    # draw scores
    canvas.draw_text(str(score1), [WIDTH/3,HEIGHT/3], 40, "Green")
    canvas.draw_text(str(score2), [WIDTH*2/3,HEIGHT/3], 40, "Green")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    paddle_acc = 4
    
    # update right paddle when key is down
    if(key == simplegui.KEY_MAP["w"]):
        paddle1_vel -= paddle_acc
    elif(key == simplegui.KEY_MAP["s"]):
        paddle1_vel += paddle_acc
        
    # update left paddle when key is down
    if(key == simplegui.KEY_MAP["up"]):
        paddle2_vel -= paddle_acc
    elif(key == simplegui.KEY_MAP["down"]):
        paddle2_vel += paddle_acc
      

   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    # stop right paddle when key is released
    if(key == simplegui.KEY_MAP["w"]) or (key == simplegui.KEY_MAP["s"]):
        paddle1_vel = 0
    elif(key == simplegui.KEY_MAP["up"]) or (key == simplegui.KEY_MAP["down"]):
        paddle2_vel = 0
        
def reset_button_handler():
    new_game()


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", reset_button_handler)


# start frame
new_game()
frame.start()
