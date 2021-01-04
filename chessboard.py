import turtle  # importing turtle package

t = turtle.Turtle()  # creating our turtle object
t.speed(10)  # declaring the speed for our turtle object

# going to the desired location which is (-160,-160)
t.penup()  
t.left(180)
t.forward(160)
t.left(90)
t.forward(160)
t.left(90)
t.pendown()

# declaring and initializing our co-ordinate variables
x = -160
y = -120

# declaring and initializing the color variable
fill_color = "black"

# prints the chessboard
for i in range(8):
    for j in range(8):
        t.begin_fill()  # begin the filling process

        for k in range(4):  # drawing the box
            t.forward(40)
            t.left(90)

        t.fillcolor(fill_color)  # filling the box
        t.end_fill()  # completing our fill
    
        # changing the color for the next block
        if fill_color == "black":
            fill_color = "white"
        elif fill_color == "white":
            fill_color = "black"
    
        t.forward(40)  # going to the next block's position 
    
    # going to the next row
    t.penup()
    t.goto(x, y)
    t.pendown()
    y = y + 40
    
    # setting the initial block color for the next row
    if fill_color == "black":
        fill_color = "white"
    elif fill_color == "white":
        fill_color = "black"

turtle.done()
