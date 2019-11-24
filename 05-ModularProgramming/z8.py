def drawSquare(x,y,n):
    import turtle
    pen = turtle.Turtle()
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()
    
    for a in range(4):
        pen.forward(n)
        pen.right(90)
    
for x in range(4):
    for y in range(4):
        drawSquare(x*100,-(y*100),100)