from turtle import Turtle

Y = -280
PADDLE_PARTS = []
for X in range(-60, 61, 10):
    new_part = (X, Y)
    PADDLE_PARTS.append(new_part)


class Paddle:
    def __init__(self):
        self.parts = []
        self.make_paddle()
        self.right = self.parts[-1]
        self.left = self.parts[0]

    def make_paddle(self):
        for pos in PADDLE_PARTS:
            part = Turtle(shape="square")
            part.color("white")
            part.penup()
            part.goto(pos)
            part.shapesize(stretch_wid=0.5)
            self.parts.append(part)

    def move_left(self):
        if self.left.xcor() < -380:
            pass
        else:
            for part in self.parts:
                new_x = part.xcor() - 20
                part.goto(new_x, -280)

    def move_right(self):
        if self.right.xcor() > 380:
            pass
        else:
            for part in self.parts:
                new_x = part.xcor() + 20
                part.goto(new_x, -280)

    def reset(self):
        for part in self.parts:
            part.ht()
        self.parts.clear()
        self.make_paddle()
        self.right = self.parts[-1]
        self.left = self.parts[0]
