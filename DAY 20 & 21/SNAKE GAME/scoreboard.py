from turtle import Turtle
ALIFNMENT = "center"
FONT = ("Arial",24,"normal")

class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("DAY 20 & 21/SNAKE GAME/data.txt") as data:
            self.high_score =int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:  {self.high_score}",align=ALIFNMENT,font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("DAY 20 & 21/SNAKE GAME/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    