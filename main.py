from utils import init_screen, init_turtles, start_race

screen = init_screen()
user_bet = screen.textinput(
    "Make your bet", "Which turtle will win the rage? Enter a color: "
)

turtles = init_turtles()
start_race(turtles, user_bet)

screen.exitonclick()
