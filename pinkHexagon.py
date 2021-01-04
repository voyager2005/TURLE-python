import turtle

colors = ['white', 'pink', 'violet', 'magenta', 'purple', 'indigo', '']  # declaring all the colors

t = turtle.Pen()  # creating the object
t.speed(10)

turtle.bgcolor('black')  # background color

for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(int(x/100) + 1)
    t.forward(x)
    print(x)
    t.left(59)

turtle.done()
