from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.color("black")
        self.penup()
        self.goto(-250, 250)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Level : {self.current_level}", font=FONT)

    def increase_level(self):
        self.current_level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(-200, 0)
        self.write(f"Game Over. You reached level {self.current_level}.", font=FONT)
