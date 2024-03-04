from turtle import Turtle,Screen
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5 , stretch_wid= 0.5)
        self.color("blue")
        self.penup()
        self.delete_turtle()
    
    def delete_turtle(self):
        self.goto(random.randint(-250,250),random.randint(-250,250))