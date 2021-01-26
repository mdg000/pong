# 100 Days of Code
# Pong Game

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# gam objects
paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-360, 0))
ball = Ball()
scoreboard = Scoreboard()

# game input controls
screen.listen()
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")

screen.onkey(paddle_2.go_up, "a")
screen.onkey(paddle_2.go_down, "z")

# game loop
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # removes starting animations
    ball.move()
    # detect collision with floor or ceiling
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with paddles
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    # detect collision with back walls
    if ball.xcor() > 380:
        ball.move_speed = 0.1
        time.sleep(0.3)
        ball.goto(0, 0)
        ball.x_move *= -1
        scoreboard.player_2_point()
    if ball.xcor() < -390:
        ball.move_speed = 0.1
        time.sleep(0.3)
        ball.goto(0, 0)
        ball.x_move *= -1
        scoreboard.player_1_point()

screen.exitonclick()

