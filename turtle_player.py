from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.xcor()
        self.ycor()
        self.penup()
        self.goto(0, -280)

    def up(self):
        self.forward(30)

    def down(self):
        self.forward(-30)

    def move_right(self):
        self.goto(self.xcor() + 10, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - 10, self.ycor())

    def get_spot(self):
        print(self.xcor())
        print(self.ycor())

    def reset_player(self):
        self.goto(0, -280)
