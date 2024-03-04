from turtle import Turtle,TK
class Scorboar(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.printHighScore()
    def IncreaseScore(self):
            self.score += 1
            return self.score    
    
    def reset(self):
        if self.score > self.high_score:
              self.high_score = self.score
        self.score = 0
    
    def found_high(self):
        with open("snake_game_scores.txt","r") as f:
            f.seek(0)
            satirlar = f.readlines()
        for satir in satirlar:
            satir = int(satir)
            self.high_score = int(self.high_score)
            if satir > self.high_score:
                self.high_score = satir
        return satir

    
    def Finish_score(self):
        self.goto(0,0)
        self.write("GAME OVER",font = ('Arial',20,'normal'),align ='center',move=True)

    def printHighScore(self):
        self.goto(70,310)
        self.write(f"Score : {self.score}  High Score : {self.found_high()}",font = ('Arial',20,'normal'),align ='center',move=True)
        
     
     
"""    def First_score(self):
        self.hideturtle()
        self.goto(-70,310)
        self.write("Score : 0",font = ('Arial',20,'normal'),align ='center',move=True)"""