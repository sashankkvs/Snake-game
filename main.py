from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from playsound import playsound
from threading import Thread
from tkinter import Button
screen = Screen()
screen.setup(width= 600, height= 650)
screen.bgcolor("black")
screen.title("The Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()
screen.onkey(key="Up", fun = snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
#
# def play():
#     playsound("Snake Game.mp3", True)

def play():
    def play_thread_function():
        playsound("Snake Game.mp3")

    play_thread = Thread(target=play_thread_function)
    play_thread.start()

play_button = Button(text="Play music", command=play)
play_button.pack()

game_play = True

while game_play:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    for segment in snake.segments[1:]:
        if snake.head == snake.segments:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
























screen.exitonclick()