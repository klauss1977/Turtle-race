from turtle import Turtle, Screen
import random
is_race_on=False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors=['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80 ]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>=225:
            screen.title(f"Winner is {turtle.pencolor()} turtle")
            screen.bgcolor(turtle.pencolor())
            is_race_on=False
            if user_bet==turtle.pencolor():
                print(f"You won! The {turtle.pencolor()} turtle is the winner")

            else:
                print(f"You lost! The {turtle.pencolor()} turtle is the winner")
        random_distance=random.randint(0,9)
        turtle.forward(random_distance)













screen.exitonclick()
