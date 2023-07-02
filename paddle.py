from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_wid=5.0, stretch_len=1.0, outline=1)
        self.color("white")
        self.goto(position)  # input start position as tuple on main

    def up(self):
        go_up = self.ycor() + 20
        self.goto(self.xcor(), go_up)

    def down(self):
        go_down = self.ycor() - 20
        self.goto(self.xcor(), go_down)
