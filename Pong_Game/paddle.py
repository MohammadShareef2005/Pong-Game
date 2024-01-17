from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.setposition(position)

    def up(self):
        if self.ycor() < 245:
            y_cor = self.ycor() + 20
            self.goto(self.xcor(), y_cor)

    def down(self):
        if self.ycor() > -245:
            y_cor = self.ycor() - 20
            self.goto(self.xcor(), y_cor)
