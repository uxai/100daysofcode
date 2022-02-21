import time, random
from turtle import Screen
from chomper import Chomper
from car import Car
from level import Level

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.title("Turtler")

player = Chomper()

cars = []
cars.append(Car())

level = Level()

screen.listen()
screen.onkey(player.move, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move()
        if car.distance(player) < 20:
            game_on = False
            level.game_over()

    random_chance = random.randint(1, 5)
    if random_chance == 1:
        cars.append(Car())
    if player.ycor() > 280:
        player.goto_start()
        level.next_level()


screen.exitonclick()