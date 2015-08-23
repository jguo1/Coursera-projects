# http://www.codeskulptor.org/#user40_ZEOJ2BHop6_10.py
# template for "Stopwatch: The Game"
import simplegui
# define global variables
time_count = 0
times = 0
bingo = 0
current_key = ' '
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = B = C = D = 0
    A = t / 600
    B = (t - A * 600) / 100 % 10
    C = (t - A * 600) / 10 % 10
    D = (t - A * 600) % 10
    return str(A)+":"+str(B)+str(C)+"."+str(D)   
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()    
def Stop():
    global times,bingo
    if timer.is_running():
        times += 1
        if (time_count - time_count / 600 * 600) % 10 == 0:
            bingo += 1
    timer.stop()

def player1():
    global times
    if timer.is_running():
        if (time_count - time_count / 600 * 600) % 10 == 0:
            times += 3
        else:
            times -= 1

def player2():
    global bingo
    if timer.is_running():
        if (time_count - time_count / 600 * 600) % 10 == 0:
            bingo += 3
        else:
            bingo -= 1
            
def player_key(key):
    if key == simplegui.KEY_MAP['q']:
        player1()
    elif key == simplegui.KEY_MAP['p']: 
        player2()
        
def Reset():
    timer.stop()
    global time_count,times,bingo
    time_count = 0
    times = 0
    bingo = 0

def Stopwatch():
    frame = simplegui.create_frame("StopWatch",300,200)
    frame.start()
    Reset()
    frame.add_button("Start",Start,100)
    frame.add_button("Stop",Stop,100)
    frame.add_button("Reset",Reset,100)
    frame.add_label('')
    frame.add_button("Dual-Game (Optional)",Dual_game,150)
    frame.set_draw_handler(draw)

    
def Dual_game():
    f = simplegui.create_frame("Dual-Game",300,200)
    f.start()
    Reset()
    f.add_button("Start",Start,150)
    f.add_button("Player1 press[q]",player1,150)
    f.add_button("Player2 press[p]",player2,150)
    f.add_button("Reset",Reset,150)
    f.set_keydown_handler(player_key)
    f.add_label('')
    f.add_button("Back to Stopwatch",Stopwatch,150)
    f.set_draw_handler(draw_dual)
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time_count
    time_count += 1
# define draw handler
def draw(canvas):
    canvas.draw_text(format(time_count), (70, 120), 60, 'White', "sans-serif")
    canvas.draw_text(str(bingo)+"/"+str(times), (230, 35), 36, 'Green', "sans-serif")
    
def draw_dual(canvas):
    canvas.draw_text(format(time_count), (70, 120), 60, 'White', "sans-serif")
    canvas.draw_text("P2:"+str(bingo), (200, 35), 36, 'Yellow', "sans-serif")
    canvas.draw_text("P1:"+str(times), (10, 35), 36, 'Red', "sans-serif")
# create frame

timer =simplegui.create_timer(100, timer_handler)
# register event handlers
#frame.add_button("Start",Start,100)
#frame.add_button("Stop",Stop,100)
#frame.add_button("Reset",Reset,100)
#frame.add_button("Dual-Game",Dual_game,100)
#frame.set_draw_handler(draw)

# start frame
Stopwatch()

# Please remember to review the grading rubric
