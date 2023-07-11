from turtle import Screen
from paddle_1 import Paddle_1
from paddle_2 import Paddle_2
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
p1 = Paddle_1()
p2 = Paddle_2()
ball = Ball()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

screen.listen()
screen.onkey(p1.move_up, "Up")
screen.onkey(p1.move_down, "Down")

screen.onkey(p2.move_up, "w")
screen.onkey(p2.move_down, "s")
timer = 0.1
game_is_on = True

while game_is_on:
    time.sleep(timer)
    screen.update()
    ball.move()

    #detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    #detect paddle collision
    if ball.distance(p1) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()
        timer *= 0.9

    elif ball.distance(p2) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
        timer *= 0.9

    #detect when ball goes out of right side
    if ball.xcor() > 380:
        ball.new_ball()
        scoreboard.increase_p2_score()
        scoreboard.display_score()
        timer = 0.1

    elif ball.xcor() < -380:
        ball.new_ball()
        scoreboard.increase_p1_score()
        scoreboard.display_score()
        timer = 0.1

screen.exitonclick()

