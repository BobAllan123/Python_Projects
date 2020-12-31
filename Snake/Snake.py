# Snake game by Bob Allan
# 12/28/2020

import turtle
import time
import random

delay = 0.12
score = 0
high_score = 0

# Snake body segments
segments = []

# Set up screen
wn = turtle.Screen()
wn.title("Snake Game by Bob Allan")
wn.bgcolor("darkblue")
wn.setup(width=600, height=600)
# turns off screen updates
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
#start in the center of the screen
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
#start in the center of the screen
food.goto(0,100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal" ))

# Functions
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

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up");
wn.onkeypress(go_down, "Down");
wn.onkeypress(go_left, "Left");
wn.onkeypress(go_right, "Right");

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor()<-290 or head.ycor() > 290 or head.ycor() <-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        #Hide the segments
        for segment in segments:
            segment.hideturtle()
        #Clear the segments
        segments.clear()
        delay = 0.12

        # Reset the score
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # where we check for a collision with food
    if head.distance(food) < 20:
        #move food
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("darkgrey")
        new_segment.penup()
        segments.append(new_segment)

        # Speed up the snake as the snake gets longer
        delay -= 0.001

        # Increase the score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal" ))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.hideturtle()

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.12

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

# keeps the window open
wn.mainloop()