import turtle

play_ground = turtle.Screen()
play_ground.title("Ping Pong")
play_ground.bgcolor("dark green")
play_ground.setup(width=800, height=600)
play_ground.tracer(0)  # stops the window from auto update so i can set the speed


# Player_1
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("red")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(-350, 0)


# Player_2
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("white")
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.penup()
player_2.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5


# Score
score = turtle.Turtle()
score.speed()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write(
    "player_1 : 0 || Player_2 : 0", align="center", font=("Courier", 24, "normal")
)


# Functions
def player_1_up():
    y = player_1.ycor()
    y += 20
    player_1.sety(y)


def player_1_down():
    y = player_1.ycor()
    y -= 20
    player_1.sety(y)


def player_2_up():
    y = player_2.ycor()
    y += 20
    player_2.sety(y)


def player_2_down():
    y = player_2.ycor()
    y -= 20
    player_2.sety(y)


# keyboard blindings
play_ground.listen()
play_ground.onkeypress(player_1_up, "Up")
play_ground.onkeypress(player_1_down, "Down")
play_ground.onkeypress(player_2_up, "w")
play_ground.onkeypress(player_2_down, "s")

# main loop
while True:
    play_ground.update()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() > -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() > -390:
        ball.goto(0, 0)
        ball.dx *= -1

    if (ball.xcor() > 340 and ball.xcor() < 350) and (
        ball.ycor() < player_1.ycor() + 40 and ball.ycor() > player_1.ycor() - 40
    ):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() > -340 and ball.xcor() < -350) and (
        ball.ycor() < player_2.ycor() + 40 and ball.ycor() > player_2.ycor() - 40
    ):
        ball.setx(-340)
        ball.dx *= -1
