from turtle import Turtle
MOVE_FORWARD = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.change_x = 10
        self.change_y = 10
        self.sleep_rate = 0.10

    def move(self):
        new_x = self.xcor() + self.change_x
        new_y = self.ycor() + self.change_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.change_y *= -1
        self.sleep_rate *= 0.9

    def bounce_x(self):
        self.change_x *= -1
        self.sleep_rate *= 0.9
    def goal(self):
        self.home()
        self.sleep_rate = 0.1
        self.bounce_x()
