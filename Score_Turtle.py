from turtle import Turtle
import random
color = ["blue", "red", "magenta", "brown", "orange", "purple"]


class Writer(Turtle):
    def __init__(self, coordinate, state):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(coordinate)
        self.color(random.choice(color))
        self.write(arg=state, font=("ariel", 10, "normal"))
