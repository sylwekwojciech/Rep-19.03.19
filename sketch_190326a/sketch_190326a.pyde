def setup():
    import random
    
    global sqsize
    sqsize = 60        
    global xpos 
    global ypos       
    global xspeed 
    xspeed = 3  
    global yspeed 
    yspeed = 2  
    global xdirection 
    xdirection = 1  
    global ydirection 
    ydirection = 1  
    
    size(700, 700)
    noStroke()
    frameRate(30)
    rectMode(CENTER)
    xpos = width/2
    ypos = height/2
   


def draw():
    global xpos 
    global ypos       
    global xspeed 
    global yspeed 
    global xdirection 
    global ydirection
    fill(random(111),random(50),random(150))# z kolorami na łatwiznę? ;)
    
    background(111)
  
    xpos = xpos + ( xspeed * xdirection )
    ypos = ypos + ( yspeed * ydirection )
    # ruch miał być od połowy krawędzi do połowy krawędzi, a program się zamykać po dojściu
  
    if (xpos > width or xpos < 0):
        xdirection *= -1
  
    if (ypos > height or ypos < 0):
        ydirection *= -1
      
    rect(xpos, ypos, sqsize, sqsize)