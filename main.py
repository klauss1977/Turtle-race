from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=900, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
finish = Turtle()
finish.speed('fastest')
finish.hideturtle()
finish.pensize(5)


def draw_finish_line():
    finish.penup()
    finish.goto(230, -250)
    for _ in range(15):
        finish.pendown()
        finish.goto(230, finish.ycor() + 20)
        finish.penup()
        finish.goto(230, finish.ycor() + 20)


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
    draw_finish_line()

for turtle in all_turtles:
    if user_bet == turtle.pencolor():
        turtle.write("BET")

while is_race_on:
    for turtle in all_turtles:

        if turtle.xcor() >= 225:
            is_race_on = False
            if user_bet == turtle.pencolor():

                turtle.write("You won!", align="center", font=("Cooper Black", 25, "italic"))

            else:
                turtle.write("You lost!", align="center", font=("Cooper Black", 25, "italic"))

        random_distance = random.randint(0, 9)
        turtle.forward(random_distance)

screen.exitonclick()
