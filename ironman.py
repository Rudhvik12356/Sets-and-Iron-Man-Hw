import pgzrun,random
from time import time

WIDTH = 1000
HEIGHT = 600

ironmans = []
lines = []

nextIronman = 0
noOfIronman = random.randint(5,8)

startTime = 0
totalTime = 0
endTime = 0

def createIronmans():
    global startTime
    
    for i in range(noOfIronman):
        ironman = Actor("ironman")
        ironman.pos = random.randint(200, WIDTH-200),random.randint(100, HEIGHT-100)
        ironmans.append(ironman)
        
    startTime = time()       

def draw():
    global totalTime
    n = 1
    
    screen.blit("city", (0,0))
    
    for i in ironmans:
        screen.draw.text(str(n), (i.pos[0], i.pos[1]+20), color = "black")
        i.draw()
        n += 1
        
    for i in lines:
        screen.draw.line(i[0], i[1], color = "black")
        
    if nextIronman < noOfIronman:
        totalTime = time()-startTime
        screen.draw.text(str(round(totalTime, 1)), (20, 20), fontsize = 30, color = "black")
    else:
        screen.draw.text(str(round(totalTime, 1)), (20, 20), fontsize = 30, color = "black")                           
    
def update():
    pass

def on_mouse_down(pos):
    global nextIronman, lines
    
    if nextIronman < noOfIronman:
        if ironmans[nextIronman].collidepoint(pos):
            if nextIronman:
                lines.append((ironmans[nextIronman-1].pos, ironmans[nextIronman].pos))
                print(lines)
                
            else:
                nextIronman = 0
                lines = []
            nextIronman+=1
createIronmans()
pgzrun.go()                          