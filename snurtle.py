import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Create a window
w = turtle.Screen()
w.title("turtle?")
w.bgcolor("blue")
w.setup(width=750, height=750)
w.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("turtle")
head.color("lime")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 320)
pen.write("High Score : 0 Score : 0", align="center",
          font=("arial", 20, "bold"))


# assigning key directions
def group():
    if head.direction != "down":
        head.direction = "up"
        head.setheading(90)  # Set the turtle's head direction
        update_followers_direction()


def godown():
    if head.direction != "up":
        head.direction = "down"
        head.setheading(270)
        update_followers_direction()


def goleft():
    if head.direction != "right":
        head.direction = "left"
        head.setheading(180)
        update_followers_direction()


def goright():
    if head.direction != "left":
        head.direction = "right"
        head.setheading(0)
        update_followers_direction()


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


def update_followers_direction():
    for follower in followers:
        follower.setheading(head.heading())


w.listen()
w.onkeypress(group, "w")
w.onkeypress(godown, "s")
w.onkeypress(goleft, "a")
w.onkeypress(goright, "d")

followers = []

while True:
    w.update()
    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        for follower in followers:
            follower.goto(1000, 1000)
        followers.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("High Score : {} Score : {}".format(
            high_score, score), align="center", font=("arial", 20, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        food.goto(x, y)

        # Adding new turtle
        new_follower = turtle.Turtle()
        new_follower.speed(0)
        new_follower.shape("turtle")
        new_follower.color("green")
        new_follower.penup()
        followers.append(new_follower)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("High Score : {} Score : {}".format(
            high_score, score), align="center", font=("arial", 20, "bold"))

    # Checking for head collisions with trail
    for index in range(len(followers) - 1, 0, -1):
        x = followers[index - 1].xcor()
        y = followers[index - 1].ycor()
        followers[index].goto(x, y)
    if len(followers) > 0:
        x = head.xcor()
        y = head.ycor()
        followers[0].goto(x, y)
    move()
    for follower in followers:
        if follower.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for follower in followers:
                follower.goto(1000, 1000)
            followers.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("High Score : {} Score : {} ".format(
                high_score, score), align="center", font=("arial", 20, "bold"))
    time.sleep(delay)
