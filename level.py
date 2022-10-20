from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-280, 255)
        self.write(f"Level {self.level}", font=("Comic Sans MS", 16, "normal"))

    def game_over(self):
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-280, -30)
        self.write("GAME OVER", font=("Comic Sans MS", 70, "bold"))

    def up_one_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", font=("Comic Sans MS", 16, "normal"))
