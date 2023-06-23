from turtle import Turtle


class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.yellow_bricks = []
        self.green_bricks = []
        self.orange_bricks = []
        self.red_bricks = []
        self.build_bricks()

    def build_bricks(self):
        for x in range(-380, 381, 50):
            for y in range(0, 21, 20):
                yellow_brick = Turtle("square")
                yellow_brick.shapesize(.5, 2.2)
                yellow_brick.color("#FFFF00")
                yellow_brick.penup()
                yellow_brick.goto(x, y)
                self.yellow_bricks.append(yellow_brick)
        for x in range(-380, 381, 50):
            for y in range(40, 61, 20):
                green_brick = Turtle("square")
                green_brick.shapesize(.5, 2.2)
                green_brick.color("#00FF00")
                green_brick.penup()
                green_brick.goto(x, y)
                self.green_bricks.append(green_brick)
        for x in range(-380, 381, 50):
            for y in range(80, 101, 20):
                orange_brick = Turtle("square")
                orange_brick.shapesize(.5, 2.2)
                orange_brick.color("#FFA500")
                orange_brick.penup()
                orange_brick.goto(x, y)
                self.orange_bricks.append(orange_brick)
        for x in range(-380, 381, 50):
            for y in range(120, 141, 20):
                red_brick = Turtle("square")
                red_brick.shapesize(.5, 2.2)
                red_brick.color("#FF0000")
                red_brick.penup()
                red_brick.goto(x, y)
                self.red_bricks.append(red_brick)
