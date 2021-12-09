from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xball_speed = 0.1
        self.yball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xball_speed
        new_y = self.ycor() + self.yball_speed
        self.goto((new_x, new_y))

    def bounceborder(self):
        self.yball_speed *= -1

    def bounce_paddle(self):
        self.xball_speed *= -1
    def reset_position(self):
        self.goto(0,0)
        self.xball_speed=0.1
        self.yball_speed=0.1
