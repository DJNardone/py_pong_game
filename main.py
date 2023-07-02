from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))  # input a tuple here for paddle start position (x, y)
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


game_in_play = True
while game_in_play:
    screen.update()
    time.sleep(ball.sleep_rate)
    ball.move()
    # detect ball collision with wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()
    # detect ball collision w/ paddles
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60\
            and ball.xcor() < -320:
        ball.bounce_x()

    # detect r_paddle miss
    if ball.xcor() > 380:
        ball.goal()
        scoreboard.l_point()

    # detect l_paddle miss
    if ball.xcor() < -380:
        ball.goal()
        scoreboard.r_point()

screen.exitonclick()