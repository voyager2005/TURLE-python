# import required modules
import turtle
import time
import random

# initialization 
delay = 0.09
score = 0
high_score = 0
keys = 0

# you can change the width and height of the screen by changing the values here
width = 1590
height = 790

# range where the food can spawn
positive_x = ((width - 20)/2)
negative_x = -((width - 20)/2)
positive_y = ((height - 20)/2)
negative_y = -((height - 20)/2)

# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")

# the width and height can be put as user's choice
wn.setup(width=width, height=height)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
colors = random.choice(['pink', 'purple', 'indigo'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

# high score and score banner
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",
          font=("consolas", 24, "bold"))


# assigning key directions
def go_up():
    global keys
    print(str(keys) + " up")
    keys = keys + 1
    if head.direction != "down":
        head.direction = "up"


def go_down():
    global keys
    print(str(keys) + " down")
    keys = keys + 1
    if head.direction != "up":
        head.direction = "down"


def go_left():
    global keys
    print(str(keys) + " left")
    keys = keys + 1
    if head.direction != "right":
        head.direction = "left"


def go_right():
    global keys
    print(str(keys) + " right")
    keys = keys + 1
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# YOU CAN CHANGE YOUR KEY BINDINGS HERE
wn.listen()
wn.onkeypress(go_up, "8")  # CHANGE YOUR GO UP KEY HERE
wn.onkeypress(go_down, "5")  # CHANGE YOUR GO DOWN KEY HERE
wn.onkeypress(go_left, "4")  # CHANGE YOUR GO LEFT KEY HERE
wn.onkeypress(go_right, "6")  # CHANGE YOUR GO RIGHT KEY HERE

segments = []

# Main Gameplay
while True:
    wn.update()
    if head.xcor() > positive_x or head.xcor() < negative_x or head.ycor() > positive_y or head.ycor() < negative_y:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.9
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("consolas", 24, "bold"))
    if head.distance(food) < 20:
        x = 100
        y = 100
        for i in range(3):
            x = random.randint(int(negative_x)+30, int(positive_x)-30)
            y = random.randint(int(negative_y)+30, int(positive_y)-30)
            food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("lime")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        if delay > 0.070:
            delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("consolas", 24, "bold"))
        # Checking for head collisions with body segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()

            score = 0
            delay = 0.09
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("consolas", 24, "bold"))
    time.sleep(delay)

wn.mainloop()
