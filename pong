# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
ball_vel = [5, 1]
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
scoreL = 0
scoreR = 0
paddle1_pos = [PAD_WIDTH / 2, HEIGHT / 2]
paddle2_pos = [WIDTH - PAD_WIDTH / 2, HEIGHT / 2]
paddle1_vel = 0
paddle2_vel = 0
paddle_vel = 8
Rpoint = True

def spawn_ball():
    global ball_pos, ball_vel, Rpoint
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if Rpoint:
        ball_vel = [(random.randrange(200,350) )/ 100, random.randrange(190,250) / -100]
    else:
        ball_vel = [random.randrange(200,350) / -100, random.randrange(190,250) / -100]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel 
    global scoreL, scoreR
    global ball_pos
    scoreL = 0
    scoreR = 0
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    paddle1_pos = [PAD_WIDTH / 2, HEIGHT / 2]
    paddle2_pos = [WIDTH - PAD_WIDTH / 2, HEIGHT / 2]
    spawn_ball()
    
def draw(canvas):
    global Rpoint, scoreL, scoreR, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    global HALF_PAD_HEIGHT
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    

    # collide and reflect off of Top and Bottom of Canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]        
     
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] >= PAD_HEIGHT /2 and paddle1_pos[1] <= (HEIGHT - PAD_HEIGHT / 2):
        paddle1_pos[1] += paddle1_vel
    else:
        paddle1_vel = 0
    if paddle2_pos[1] >= PAD_HEIGHT /2 and paddle2_pos[1] <= (HEIGHT - PAD_HEIGHT / 2):	
        paddle2_pos[1] += paddle2_vel
    else:
        paddle2_vel = 0
    
    # draw Left paddles
    pad1top =  [paddle1_pos[0], paddle1_pos[1] - HALF_PAD_HEIGHT]
    pad1bot =  [paddle1_pos[0], paddle1_pos[1] + HALF_PAD_HEIGHT]
    canvas.draw_line(pad1top, pad1bot, PAD_WIDTH, "White")
    
    # draw Right paddles
    pad2top =  [paddle2_pos[0], paddle2_pos[1] - HALF_PAD_HEIGHT]
    pad2bot =  [paddle2_pos[0], paddle2_pos[1] + HALF_PAD_HEIGHT]
    canvas.draw_line(pad2top, pad2bot, PAD_WIDTH, "White")
    
    # determine whether paddle and ball collide
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS):
        if (paddle1_pos[1] - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos[1] + HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = ball_vel[0] * 1.2
            ball_vel[1] = ball_vel[1] * 1.2
        else:
            scoreR += 1
            Rpoint = True
            spawn_ball()
            
    if (ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS):
        if (paddle2_pos[1] - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos[1] + HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = ball_vel[0] * 1.2
            ball_vel[1] = ball_vel[1] * 1.2
        else:
            scoreL += 1
            Rpoint = False
            spawn_ball()
        
    # draw scores
    canvas.draw_text("Player 1:  " + str(scoreL), [WIDTH / 2 - 200, 30], 30, "White")
    canvas.draw_text("Player 2:  " + str(scoreR), [WIDTH / 2 + 40, 30], 30, "White")

        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle_vel
    if key == simplegui.KEY_MAP["down"]:
        if paddle2_pos[1] < HEIGHT - PAD_HEIGHT / 2:
            paddle2_vel = paddle_vel
            paddle2_pos[1] += paddle2_vel
        else:
            paddle2_vel=0
    elif key == simplegui.KEY_MAP["up"]:
        if paddle2_pos[1] > PAD_HEIGHT / 2:
            paddle2_vel = -paddle_vel
            paddle2_pos[1] += paddle2_vel
        else:
            paddle2_vel=0
    elif key == simplegui.KEY_MAP["s"]:
        if paddle1_pos[1] < HEIGHT - PAD_HEIGHT / 2:
            paddle1_vel = paddle_vel
            paddle1_pos[1] += paddle1_vel
        else:
            paddle1_vel=0
    elif key == simplegui.KEY_MAP["w"]:
        if paddle1_pos[1] > PAD_HEIGHT / 2:
            paddle1_vel = -paddle_vel
            paddle1_pos[1] += paddle1_vel
        else:
            paddle1_vel=0
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 80)

# start frame
frame.start()
new_game()
