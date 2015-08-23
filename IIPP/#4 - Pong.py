# http://www.codeskulptor.org/#user40_DUn0ADeMWy_7.py
# Implementation of classic arcade game Pong

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
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
paddle2_pos = [WIDTH - 1 - HALF_PAD_WIDTH, HEIGHT/2]
paddle1_vel = 0 
paddle2_vel = 0
p_r = 0 #pause_resume

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [0, 0]
    if direction:
        ball_vel[0] += -1 * random.randrange(60, 180) / 60.0
    else:
        ball_vel[0] += random.randrange(60, 180) / 60.0
    ball_vel[1] += -1 * random.randrange(30, 240) / 60.0
    
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,ball_vel,p_r  # these are numbers
    global score1, score2  # these are ints
    score1 = score2 = p_r = 0
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [0, 0]
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
    paddle2_pos = [WIDTH - 1 - HALF_PAD_WIDTH, HEIGHT/2]
    paddle1_vel = 0 
    paddle2_vel = 0
    spawn_ball(score1-score2)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel,player1,player2
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'red', 'White')
    # update ball
    if p_r % 2 == 0: #Judge if the pause status
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1] 
    # update paddle's vertical position, keep paddle on the screen
    # paddle1
        paddle1_pos[1] += paddle1_vel
        if paddle1_pos[1] + HALF_PAD_HEIGHT > HEIGHT - 1:
            paddle1_pos[1] = HEIGHT - 1 - HALF_PAD_HEIGHT
        elif paddle1_pos[1] - HALF_PAD_HEIGHT < 0:
            paddle1_pos[1] = HALF_PAD_HEIGHT 
      
        # paddle2
        paddle2_pos[1] += paddle2_vel
        if paddle2_pos[1] + HALF_PAD_HEIGHT > HEIGHT - 1:
            paddle2_pos[1] = HEIGHT - 1 - HALF_PAD_HEIGHT
        elif paddle2_pos[1] - HALF_PAD_HEIGHT < 0:
            paddle2_pos[1] = HALF_PAD_HEIGHT
    else:
        pass
    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos[1] + HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT),(PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT), (0, paddle1_pos[1] - HALF_PAD_HEIGHT)],1, 'white', 'white')
    canvas.draw_polygon([(WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT), (WIDTH - PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT),(WIDTH - PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT),(WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT)],1, 'white','white')
    # determine whether paddle and ball collide
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if (ball_pos[1] <= paddle1_pos[1] + HALF_PAD_HEIGHT and ball_pos[1] >= paddle1_pos[1] - HALF_PAD_HEIGHT):
            ball_vel[0] = -1.1 * ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1]
        else:
            score2 += 1
            spawn_ball(LEFT)
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if (ball_pos[1] <= paddle2_pos[1] + HALF_PAD_HEIGHT and ball_pos[1] >= paddle2_pos[1] - HALF_PAD_HEIGHT):
            ball_vel[0] = -1.1 * ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1]
        else:
            score1 += 1
            spawn_ball(RIGHT)
    elif ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - 1 - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    else:
        pass
    # draw scores
    canvas.draw_text(str(score1), (150, 50), 30, 'white',"sans-serif")  
    canvas.draw_text(str(score2), (450, 50), 30, 'white',"sans-serif")
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 8
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= vel
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += vel
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= vel
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += vel
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    
def pause_resume():
    global p_r
    p_r += 1
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New game",new_game,150)
frame.add_label('', 20)
frame.add_button("Pause / Resume",pause_resume,150)



# start frame
new_game()
frame.start()
