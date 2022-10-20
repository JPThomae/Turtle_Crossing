from turtle import Turtle
import random

COLORS = ["blue", "gray", "red", "yellow", "orange", "green"]
CAR_SIZE = [2, 3, 4]
STARTING_LOCATIONS = [-250, -220, -190, -160, -130, -100, -70, -40, -10,
                      20, 50, 80, 110, 140, 170, 200, 230]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.xcor()
        self.ycor()
        self.car_type = random.choice(CAR_SIZE)
        self.shapesize(stretch_wid=1, stretch_len=self.car_type)
        self.goto(random.randint(-290, 290), random.choice(STARTING_LOCATIONS))
        self.tire1 = Turtle()
        self.tire2 = Turtle()
        self.set_tires()

    def set_tires(self):
        self.tire1.shape("circle")
        self.tire1.shapesize(stretch_len=.5, stretch_wid=.5)
        self.tire1.color("black")
        self.tire1.penup()
        self.tire1.goto(self.xcor() + 15, self.ycor() - 10)
        self.tire2.shape("circle")
        self.tire2.shapesize(stretch_len=.5, stretch_wid=.5)
        self.tire2.color("black")
        self.tire2.penup()
        self.tire2.goto(self.xcor() - 15, self.ycor() - 10)

    def move_car(self):
        self.forward(10)

    def reset_car(self):
        self.goto(310, self.ycor())

    def kill_check(self, player):
        if self.car_type == 2 and player.distance(self) < 15:
            return True
        if self.car_type == 3 and player.distance(self) < 25:
            return True
        if self.car_type == 4 and player.distance(self) < 35:
            return True
