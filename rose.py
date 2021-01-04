import turtle

colors = ['red', 'red', 'red', 'red', 'red', 'red']  # declaring all the colors

t = turtle.Pen()  # creating the object
t.speed(100)

turtle.bgcolor('black')  # background color

for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(int(x/100) + 1)
    t.forward(x)
    t.left(49)

turtle.done()
