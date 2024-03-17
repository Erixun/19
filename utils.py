from random import randint
from turtle import Screen, Turtle


def init_turtles(colors=["red", "orange", "yellow", "green", "blue", "purple"]):
    turtles = []
    for i, color in enumerate(colors):
        turtle = Turtle("turtle")
        turtle.color(color)
        turtle.penup()
        turtle.goto(-230, -100 + i * 50)
        turtles.append(turtle)
    return turtles


def init_screen():
    screen = Screen()
    screen.setup(width=500, height=400)
    screen.colormode(255)
    return screen


def random_rgb(cmode=255):
    red = randint(1, cmode)
    green = randint(1, cmode)
    blue = randint(1, cmode)

    return red, green, blue


def onward(turtles: list[Turtle]):
    for turtle in turtles:
        step = randint(5, 25)
        turtle.forward(step)


def check_winner(turtles: list[Turtle]):
    for turtle in turtles:
        if turtle.xcor() > 220:
            return turtle.pencolor()


def start_race(turtles: list[Turtle], bet: str):
    winner = None
    while winner is None:
        onward(turtles)
        winner = check_winner(turtles)

    print(f"The winner is {winner}!")
    print(f"You were {'right' if winner == bet else 'wrong'} to bet on {bet}.")
