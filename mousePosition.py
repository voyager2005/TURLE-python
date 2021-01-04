import turtle


def motion(event):
    x = event.x - 386
    y = event.y

    if y > 327:
        y = y - 327
    elif y < 327:
        y = 327 - y
    elif y == 327:
        y = 0
    print('{}, {}'.format(x, y))


canvas = turtle.getcanvas()
canvas.bind('<Motion>', motion)

turtle.done()
