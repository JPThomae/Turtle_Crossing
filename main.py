import time
from turtle import Screen
from turtle_player import Player
from level import Scoreboard
from cars import Car


def move():
    tv.onkeypress(turtle.up, "Up")
    tv.onkeypress(turtle.down, "Down")
    tv.onkeypress(turtle.move_right, "Right")
    tv.onkeypress(turtle.move_left, "Left")
    tv.onkeypress(turtle.get_spot, "space")


def add_cars():
    for _ in range(1, 6):
        extra_car = Car()
        cars.append(extra_car)


tv = Screen()
tv.setup(width=600, height=600)
tv.tracer(0)
tv.listen()
turtle = Player()
level = Scoreboard()
game_speed = .15
number_of_cars = 31

cars = []
for _ in range(1, number_of_cars):
    car = Car()
    cars.append(car)

game_on = True
while game_on:
    tv.update()
    move()
    for car in cars:
        car.forward(10)
        car.set_tires()
        if car.xcor() < -310:
            car.reset_car()
        if turtle.ycor() == car.ycor():
            if car.kill_check(turtle):
                level.game_over()
                game_on = False
    if turtle.ycor() >= 260:
        tv.update()
        time.sleep(3)
        level.up_one_level()
        turtle.reset_player()
        add_cars()
        game_speed -= .01

    time.sleep(game_speed)

tv.exitonclick()
