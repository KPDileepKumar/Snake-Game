from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)
screen.bgcolor("black")
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()
    if (snake.head.distance(food)) < 15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    if snake.head.xcor() > 285 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -285:
        snake.reset()
        score.reset()

        # score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            score.reset()


            # score.game_over()

#screen.exitonclick()
