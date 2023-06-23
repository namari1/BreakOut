from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.9, .9)
        self.goto(0, -250)
        self.color("#D3D3D3")
        self.x_move = -12
        self.y_move = 12
        self.move_speed = .07

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def increase_speed(self):
        self.move_speed *= .98

    def bounce(self):
        self.y_move *= -1

    def vert_wall_bounce(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, -250)
        time.sleep(.8)
        self.bounce()
