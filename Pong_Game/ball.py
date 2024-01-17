from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.spe = 0.1
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.x_co = 10
        self.y_co = 10

    def move(self):
        new_x = self.xcor() + self.x_co
        new_y = self. ycor() + self.y_co
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_co *= -1
        self.spe *= 0.9

    def x_bounce(self):
        self.x_co *= -1
        self.spe *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.spe = 0.1
        self.x_bounce()
