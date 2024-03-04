from turtle import Turtle,Screen
from snake_game_food import Food
from snake_class import Snake
from snake_game_scoreboard import Scorboar
import time
from os import system
screen = Screen()
continue_game = True
screen.tracer(0)
screen.setup(width=1000 , height=700)
screen.bgcolor("black")
screen.title("My Snake Game")
lines = Turtle()
lines.pensize(20)
lines.speed("fastest")
lines.hideturtle()
lines.color("white")
lines.penup()
lines.goto(-300,300)
lines.pendown()
lines.forward(600)
lines.right(90)
lines.forward(600)
lines.right(90)
lines.forward(600)
lines.right(90)
lines.forward(600)

def stopp():
    global continue_game
    continue_game = False
    screen.bye()
snake1 = Snake()
food= Food()
write2 = Scorboar()
screen.listen()
screen.onkey(snake1.up,"Up")
screen.onkey(snake1.down,"Down")
screen.onkey(snake1.right,"Right")
screen.onkey(snake1.left,"Left")
screen.onkey(stopp,"q")
while continue_game:
    screen.update()
    snake1.move()
    time.sleep(0.1)
    write2.printHighScore()
    if -295 <snake1.square_object_list[0].xcor() < 295 and  -295 < snake1.square_object_list[0].ycor() < 295:
        pass
    else:
        write2.printHighScore()
        write2.reset()
        if write2.high_score> write2.found_high():
            with open("snake_game_scores.txt", "w") as filee:
                filee.write(f"{write2.high_score}")
                filee.seek(0)
        else:
            pass
        write2.high_score = int(write2.high_score)
        write2.clear()
        snake1.resetSnake()
    if (snake1.square_object_list[0].distance(food)) < 15 :
        write2.IncreaseScore()
        food.delete_turtle()
        write2.clear()
        write2.printHighScore()
        snake1.add_body()
    if len(snake1.square_object_list) > 3:
        for segment in snake1.square_object_list[1:]:
            if snake1.square_object_list[0].distance(segment)<10:
                write2.printHighScore()
                write2.reset()
            if write2.high_score> write2.found_high():
                with open("snake_game_scores.txt", "w") as filee:
                    filee.write(f"{write2.high_score}")
                    filee.seek(0)
           
                write2.high_score = int(write2.high_score)
                write2.clear()
                write2.reset()
                write2.printHighScore()
                snake1.resetSnake()
                
    else:
        pass
    
screen.exitonclick()