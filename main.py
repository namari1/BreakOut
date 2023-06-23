from turtle import Screen
from paddle_parts import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("BreakOut")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

playing = True
turns = 3
red = 0
orange = 0
paddle_hits = 0

while playing:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with paddle
    for part in paddle.parts:
        if ball.distance(part) < 30 and ball.ycor() < -225:
            ball.bounce()
            paddle_hits += 1
            break

    if paddle_hits == 4 or paddle_hits == 12:
        ball.increase_speed()

    if orange == 1:
        orange += 1
        ball.increase_speed()

    if red == 1:
        red += 1
        ball.increase_speed()

    # detect collision with vertical walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.vert_wall_bounce()

    # detect collision with top wall
    if ball.ycor() > 280:
        ball.bounce()

    # detect out of bounds ball
    if ball.ycor() < -280:
        ball.reset_ball()
        paddle.reset()
        turns -= 1
        scoreboard.decrease_lives()

    # detect collision with yellow bricks
    for yellow_brick in bricks.yellow_bricks:
        if ball.distance(yellow_brick) < 25:
            ball.bounce()
            yellow_brick.ht()
            bricks.yellow_bricks.remove(yellow_brick)
            scoreboard.yellow_score()

    # detect collision with green bricks
    for green_brick in bricks.green_bricks:
        if ball.distance(green_brick) < 25:
            ball.bounce()
            green_brick.ht()
            bricks.green_bricks.remove(green_brick)
            scoreboard.green_score()

    # detect collision with orange bricks
    for orange_brick in bricks.orange_bricks:
        if ball.distance(orange_brick) < 25:
            ball.bounce()
            orange_brick.ht()
            bricks.orange_bricks.remove(orange_brick)
            scoreboard.orange_score()
            orange += 1

    # detect collision with red bricks
    for red_brick in bricks.red_bricks:
        if ball.distance(red_brick) < 25:
            ball.bounce()
            red_brick.ht()
            bricks.red_bricks.remove(red_brick)
            scoreboard.red_score()
            red += 1

    # GAME OVER IF LIVES ARE OUT
    if turns == 0:
        scoreboard.reset()
        scoreboard.game_over()
        playing = False

screen.exitonclick()
