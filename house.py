import turtle

t = turtle.Turtle()
t.speed(10)
distance = 100

# drawing the square
t.left(90)
t.forward(distance)
t.left(90)
t.forward(distance)
t.left(90)
t.forward(distance)
t.left(90)
t.forward(distance)

# drawing the parallelogram (front portion of the house)
t.left(10)
t.forward(200)
t.left(80)
t.forward(distance)
t.left(100)
t.forward(200)

# drawing the triangle
t.right(10)  # straighting t
t.right(60)
t.forward(100)
t.left(120)
t.forward(100)

t.goto(-50, 187)

# drawing the roof
t.left(120)
t.left(10)
t.forward(200)
t.goto(198, 134)

# drawing the door
t.penup()
t.goto(91, 16)
t.pendown()

t.left(80)
t.forward(60)
t.right(80)
t.forward(30)
t.right(90)
t.goto(121, 23)

t.penup()
t.goto(500, 500)
t.pendown()

turtle.done()
