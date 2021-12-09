import turtle as t

class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, False, "center", ("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, False, "center", ("Courier", 70, "normal"))

