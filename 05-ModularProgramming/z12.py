from turtle import *
def drawSquare(x,y,n):
    up()
    setposition(x,y)
    down()
    for l in range(4):
        pen.forward(n)
        pen.right(90)

def drawCircle(x,y,r):
    up()
    setposition(x,y)
    down()
    circle(r)

def drawTriangle(x,y,m):
    up()
    setposition(x,y)
    down()
    forward(m)
    left(120)
    forward(m)
    left(120)
    forward(m)
    
def drawStar(x,y,n):
    up()
    setposition(x,y)
    down()
    for x in range(5):
        forward(n)
        right(144)
        forward(n)
        left(72)
 
def drawSquareColor(x,y,m,kolor):
    color(kolor)
    begin_fill()
    up()
    setposition(x,y)
    down()
    for x in range(4):
        forward(m)
        right(90)
    end_fill()

def drawChessboard(m):
    for x in range(8):
        for y in range(8):
            up()
            setposition(x*m,y*m)
            down()
            if (x%2==0 and y%2==0) or (x%2!=0 and y%2!=0):
                drawSquareColor(x*m,y*m,m,'black')
            else:
                drawSquareColor(x*m,y*m,m,'white')
    up()
    setposition(0,m*7)
    down()
    for z in range(4):
        forward(m*8)
        right(90)