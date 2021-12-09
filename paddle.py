from turtle import Turtle

move_speed = 0.2


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=0.4, stretch_len=5)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < 245:
            self.forward(15)

    def down(self):
        if self.ycor() > -245:
            self.backward(15)
