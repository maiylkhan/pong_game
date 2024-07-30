import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(800, 600)
screen.tracer(0)

r_paddle = Paddle(360, 0)
l_paddle = Paddle(-360, 0)

ball = Ball()
scoreboard = Scoreboard()
screen.listen()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
game_is_on = True


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    scoreboard.update_scoreboard()
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and 360 > ball.xcor() > 330 or ball.distance(l_paddle) < 50 and -360 < ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
