from turtle import Turtle

COLOR = "white"


class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(COLOR)
        self.speed("fast")
        self.width(5)
        self.penup()
        self.goto(0, -275)
        self.left(90)
        while self.ycor() < 300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
