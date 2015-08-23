# http://www.codeskulptor.org/#user40_ZEOJ2BHop6_3.py
# template for "Stopwatch: The Game"
import simpleguitk as simplegui
# define global variables
time_count = 0
times = 0
bingo = 0
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
    
def Reset():
    timer.stop()
    global time_count,times,bingo
    time_count = 0
    times = 0
    bingo = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time_count
    time_count += 1
# define draw handler
def draw(canvas):
    canvas.draw_text(format(time_count), (70, 120), 60, 'White', "sans-serif")
    canvas.draw_text(str(bingo)+"/"+str(times), (235, 35), 36, 'Green', "sans-serif")
    
# create frame
frame = simplegui.create_frame("StopWatch",300,200)
timer =simplegui.create_timer(100, timer_handler)
# register event handlers
frame.add_button("Start",Start,100)
frame.add_button("Stop",Stop,100)
frame.add_button("Reset",Reset,100)
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric
