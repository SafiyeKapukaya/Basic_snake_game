
from turtle import Turtle

class Snake():
    def __init__(self):
        self.square_object_list = []
        self.create_snake()
    
    def create_snake(self):
        x = -40
        y = 0  
        for square in range(0, 3):
            square = Turtle("square")
            square.speed("fastest")
            square.color("white")
            square.penup()
            square.goto(x, y)
            self.square_object_list.append(square)
            x += 20
    
    def move(self):
        for seg_num in range(len(self.square_object_list) - 1, 0, -1):
            new_x = self.square_object_list[seg_num - 1].xcor()
            new_y = self.square_object_list[seg_num - 1].ycor()
            self.square_object_list[seg_num].goto(new_x, new_y)
        
        
        if -295 < self.square_object_list[0].xcor() < 295 and -295 < self.square_object_list[0].ycor() < 295:
            self.square_object_list[0].forward(20)
        else:
          
            self.resetSnake()

    def up(self):
        if self.square_object_list[0].heading() != 270:
            self.square_object_list[0].setheading(90)
    
    def down(self):
        if self.square_object_list[0].heading() != 90:
            self.square_object_list[0].setheading(270)
    
    def left(self):
        if self.square_object_list[0].heading() != 0:
            self.square_object_list[0].setheading(180)
    
    def right(self):
        if self.square_object_list[0].heading() != 180:
            self.square_object_list[0].setheading(0)
    
    def add_body(self):
        finish_x = len(self.square_object_list) - 1
        x = self.square_object_list[finish_x].xcor() - 10
        y = self.square_object_list[finish_x].ycor() - 10  
        for _ in range(1):
            square = Turtle("square")
            square.setposition(x, y)
            square.penup()
            square.speed("fastest")
            square.color("white")
            self.square_object_list.append(square)
    
    def resetSnake(self):
        for segment in self.square_object_list:
            segment.goto(1000, 1000) 
        self.square_object_list.clear()
        self.create_snake()
