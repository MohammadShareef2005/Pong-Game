import time
from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import ScoreBoard

tur_lis = []
axis_list = [(350, 20), (350, 0), (350, -20)]
screen = Screen()
ba = Ball()
scr_bor = ScoreBoard()


screen.tracer(0)
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")


screen.listen()

pad1 = Paddle((370, 0))
pad2 = Paddle((-370, 0))
screen.onkey(pad1.up, "Up")
screen.onkey(pad1.down, "Down")
screen.onkey(pad2.up, "w")
screen.onkey(pad2.down, "s")
game_on = True
while game_on:

    screen.update()
    time.sleep(ba.spe)
    ba.move()
    if ba.ycor() > 280 or ba.ycor() < -280:
        ba.y_bounce()

    if ba.distance(pad1) < 50 and ba.xcor() > 340 or ba.distance(pad2) < 50 and ba.xcor() < -340:
        ba.x_bounce()

    if ba.xcor() > 380:
        ba.reset_position()
        scr_bor.l_point()

    if ba.xcor() < -380:
        ba.reset_position()
        scr_bor.r_point()

screen.exitonclick()
