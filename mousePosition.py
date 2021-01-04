import turtle

# place code from here to 
def motion(event):
    x = event.x - 386
    y = event.y

    if y > 326:
        y = -(y - 326)
    elif y < 326:
        y = 326 - y
    elif y == 326:
        y = 0
    print('{}, {}'.format(x, y))


canvas = turtle.getcanvas()
canvas.bind('<Motion>', motion)
# here in your program to get the location of your mouse

turtle.done()
