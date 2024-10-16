from turtle import Screen
from paddles import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(paddle1.up, "Up")
screen.onkeypress(paddle1.down, "Down")
screen.onkeypress(paddle2.up, "w")
screen.onkeypress(paddle2.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    #detect collision with top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #detect if paddle 1 missed the ball
    if ball.xcor() > 400:
        ball.reset_position()
        score.score_2_point()

    if ball.xcor() < -400:
        ball.reset_position()
        score.score_1_point()

screen.exitonclick()
