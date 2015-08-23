# pingpong
# http://www.codeskulptor.org/#user40_NVO3Vmm0wy_4.py
# 乒乓球
import simplegui
import random

WIDTH = 400
HEIGHT = 600       
BALL_RADIUS = 50
PAD_WIDTH = 80
PAD_HEIGHT = 15
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddle_vel = 0
paddle_pos = [WIDTH/2,HEIGHT - HALF_PAD_HEIGHT]
BALL_RADIUS = 5
ball_pos = [0, 0]
ball_vel = [0, 0]
BRICK_WIDTH = 40
BRICK_HEIGHT = 15
BRICK_pos = 100
BRICK_layer = 5
brick = []
count = 0
remain = BRICK_layer * 2
# 初始化brick
BRICK_number = WIDTH // BRICK_WIDTH #每行砖块数
for j in range(BRICK_layer):
    for i in range(BRICK_number):
        brick.append([i * BRICK_WIDTH,BRICK_pos - j * BRICK_HEIGHT])

# 修正小球和板子的位置，并不是真正重置游戏   
def new_game():
    global brick,BRICK_pos,ball_pos,ball_vel,BRICK_number,remain
    paddle_pos = [WIDTH/2,HEIGHT - HALF_PAD_HEIGHT]
    ball_pos = [WIDTH/2, HEIGHT - PAD_HEIGHT -BALL_RADIUS]
    ball_vel = [0, 0]

  
 # 重置游戏！
def ini_brick():
    new_game()
    global count,remain
    remain = BRICK_layer * 2
    count = 0
    for j in range(BRICK_layer):
        for i in range(BRICK_number):
            brick[i+j*BRICK_number][0] = i * BRICK_WIDTH
            brick[i+j*BRICK_number][1] = BRICK_pos - j * BRICK_HEIGHT
    
def draw(canvas):
    global brick,BRICK_pos,ball_pos,paddle_pos,BRICK_number,count,remain
    
    #draw paddel
    if paddle_pos[0] + HALF_PAD_WIDTH > WIDTH - 1:
        paddle_pos[0] = WIDTH - 1 - HALF_PAD_WIDTH
    elif paddle_pos[0] - HALF_PAD_WIDTH < 0:
        paddle_pos[0] = HALF_PAD_WIDTH 
    else:
        paddle_pos[0] += paddle_vel
    canvas.draw_polygon([(paddle_pos[0] - HALF_PAD_WIDTH, paddle_pos[1] + HALF_PAD_HEIGHT ), (paddle_pos[0] - HALF_PAD_WIDTH, paddle_pos[1] - HALF_PAD_HEIGHT),(paddle_pos[0] + HALF_PAD_WIDTH, paddle_pos[1] - HALF_PAD_HEIGHT), (paddle_pos[0] + HALF_PAD_WIDTH, paddle_pos[1] + HALF_PAD_HEIGHT)],1, 'white', 'white')
    
    # draw bricks
    for i in range(BRICK_number * BRICK_layer):
        canvas.draw_polygon([(brick[i][0],brick[i][1]),(brick[i][0],brick[i][1] + BRICK_HEIGHT),(brick[i][0]+BRICK_WIDTH,brick[i][1] + BRICK_HEIGHT),(brick[i][0]+BRICK_WIDTH,brick[i][1])],1,'black','white')
    # draw ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1] 
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'Red','red')
    
    # draw remianing attempts time
    canvas.draw_text("Opportunities left: ", (220, 20), 18, 'white',"sans-serif")
    canvas.draw_text(str(remain), (370, 20), 18, 'Yellow',"sans-serif")
    
    # determine whether paddle and ball collide
    if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= WIDTH - 1 - BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - PAD_HEIGHT -BALL_RADIUS:
        if ball_pos[0] >= paddle_pos[0] - HALF_PAD_WIDTH and ball_pos[0] <= paddle_pos[0] + HALF_PAD_WIDTH :
            ball_vel[1] = -1.05 * ball_vel[1]
            #给球加上pad的辅助速度
            if ball_vel[0] <= 10 and ball_vel[0] >= -10 and ball_pos != [WIDTH/2, HEIGHT - PAD_HEIGHT -BALL_RADIUS]:
                if paddle_vel > 0:
                    ball_vel[0] = ball_vel[0] + paddle_vel - 3
                elif paddle_vel < 0:
                    ball_vel[0] = ball_vel[0] + paddle_vel + 3
        else:
            if remain == 0:
                ini_brick()
            else:
                new_game()

    # determine brick collide 
    for j in range(BRICK_layer):
        if  ball_pos[1] <= BRICK_pos + BRICK_HEIGHT + BALL_RADIUS - j*BRICK_HEIGHT and ball_pos[1] >= BRICK_pos - BALL_RADIUS - j*BRICK_HEIGHT :
            for i in range(BRICK_number):
                #正面反弹
                if ball_pos[0] >= brick[i+ j*BRICK_number][0] and ball_pos[0] < brick[i+ j*BRICK_number][0] + BRICK_WIDTH:
                    ball_vel[1] = - ball_vel[1]
                    brick[i + j*BRICK_number][0] = 1000 #把brick[i]移走
                    count += 1
                #侧面反弹
#                elif ball_pos[1] <= BRICK_pos + BRICK_HEIGHT and ball_pos[1] >= BRICK_pos - BRICK_HEIGHT * (BRICK_layer -1):
#                    if ball_pos[0] == brick[i + j*BRICK_number][0] - BALL_RADIUS or ball_pos[0] == brick[i + j*BRICK_number][0] +BRICK_WIDTH + BALL_RADIUS:
#                        ball_vel[0] = - ball_vel[0]
#                        brick[i + j*BRICK_number][0] = 1000

                #判断砖块有没有打完   
                if count == BRICK_number * BRICK_layer: 
                    ini_brick()
                    

def keydown(key):
    vel = 8
    global paddle_vel,remain
    if key == simplegui.KEY_MAP['left']:
        paddle_vel -= vel
    elif key == simplegui.KEY_MAP['right']:
        paddle_vel += vel
    elif key == simplegui.KEY_MAP['space'] and ball_pos == [WIDTH/2, HEIGHT - PAD_HEIGHT -BALL_RADIUS]:
        ball_vel[0] = random.randrange(-600,600)/100.0 
        ball_vel[1] = -5
        remain -= 1
def keyup(key):
    global paddle_vel
    if key == simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['right']:
        paddle_vel = 0

def layer(input):
    global BRICK_layer
    if int(input)< 1:
        BRICK_layer = 1
    elif int(input)> 5:
        BRICK_layer = 5
    else:
        BRICK_layer = int(input)
    ini_brick()
    
frame = simplegui.create_frame("PingPong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game",ini_brick,100)
frame.add_label('')
frame.add_input('BRICK layer (1 to 5)', layer, 100)
frame.start()
new_game()
