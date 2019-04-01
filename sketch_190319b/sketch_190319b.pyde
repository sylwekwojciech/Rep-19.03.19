#lista = [1,2,3]
#krotka = (1,1,2)
#slownik = {"klucz":"wartosc", "key":"value"}
#zbior = {3,1,2}


def setup():
    frameRate(60)
    rectMode(CENTER)
    size(400,400)
    global x
    global y
    x=0
    y=0
    fill(0,0,255)

    strokeWeight(8)
    krotkaKolorow=((255,0,0), (0,255,0), (0,0,255))  
    stroke(*krotkaKolorow[0]) 

def draw():
    global y
    y = y + 1
    global x
    x = x + 1
    rect(height/2,width/2,x,y)
    if x > width:
        exit()
    
#def mousePressed():    
    #oop()
    #oLoop()
    #edraw()