from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

player_one = Paddle(350, 0)
player_two = Paddle(-350, 0)

ball = Ball()
p1_score = Scoreboard(-80, 200)
p2_score = Scoreboard(80, 200)

screen.listen()
screen.onkey(player_one.up, "Up")
screen.onkey(player_one.down, "Down")
screen.onkey(player_two.up, "w")
screen.onkey(player_two.down, "s")

game = True
while game:
    ball.move()
    screen.update()

    # Detect collision with ceiling and floor
    if ball.ycor() > 290 or ball.ycor() < -285:
        ball.wall_bounce()
    
    if ball.distance(player_one) < 35 and ball.xcor() > 320 or ball.distance(player_two) < 45 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 395:
        ball.reset()
        p2_score.add_score()
    
    if ball.xcor() < -395:
        ball.reset()
        p1_score.add_score()

screen.exitonclick()