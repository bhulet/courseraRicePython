"Stopwatch: The Game"

import simplegui


# define global variables
interval = 100
count, sec, min, y, x = 0, 0, 0, 0, 0
ratio = str(x) + "/" + str(y)
time = str(min) + ":" + str(sec) + "." + str(count)
game = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global count, sec, min, time
    t = count
    if (t==10):
        sec += 1
        if (sec == 60):
            min += 1
            sec = 0
        count = 0
    if (sec < 10) and (min < 10):
            time = str(0) + str(min) + ":" + str(0) + str(sec) + "." + str(count)
    elif (sec >= 10) and (min < 10):
        time = str(0) + str(min) + ":" + str(sec) + "." + str(count)
    elif (min >= 10) and (sec >= 10):
         time = str(min) + ":" + str(sec) + "." + str(count)
    elif (min >= 10) and (sec < 10):
        time = str(min) + ":" + str(0) + str(sec) + "." + str(count)
    return time
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler():
    global game
    game = True
    timer.start()
    

def stop_button_handler():
    global x, y, ratio, game, count
    if game and (count == 0):
        y += 1
        x += 1
        ratio = str(x) + "/" + str(y)
        game = False
    elif game:
        y += 1
        ratio = str(x) + "/" + str(y)
        game = False
    timer.stop()



def reset_button_handler():
    global count, min, sec, x, y, ratio, game    
    count, min, sec, x, y = 0, 0, 0, 0, 0
    ratio = str(x) + "/" + str(y)
    timer.stop()
    

# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count += 1


# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(count), [65, 105], 24, "White")
    canvas.draw_text(ratio, [155, 30], 24, "Yellow")

# create frame
frame = simplegui.create_frame("Stopwatch", 200, 200)
frame.add_button("Start", start_button_handler, 80)
frame.add_button("Stop", stop_button_handler, 80)
frame.add_button("Reset", reset_button_handler, 80)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(interval, tick)

# register event handlers

# start frame
frame.start()

