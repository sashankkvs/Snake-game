from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        with open("data.txt") as data:
            self.high_score= int(data.read())

        self.updated_score()
    def updated_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align=ALIGN, font=FONT)
        
    def reset(self):

        if self.score>self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0

        self.updated_score()
        
    # def snake_hit(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align= ALIGN, font=FONT)
    # def retry(self):
    #     self.goto(0, -30)
    #     self.write("Do you want to retry", align = ALIGN, font = FONT)

    def increase_score(self):
        self.score +=1
        self.updated_score()


