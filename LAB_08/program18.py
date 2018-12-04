import random
import turtle

turtle.speed(0)
turtle.hideturtle()
turtle.goto(600, 0)
turtle.goto(-600, 0)
turtle.goto(0, 0)
turtle.goto(0, 600)
turtle.goto(0, -600)
turtle.goto(0, 0)
turtle.penup()
turtle.setheading(90)
turtle.forward(200)
turtle.pendown()
turtle.setheading(180)
turtle.circle(200)
turtle.forward(200)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(200)


def dot_color(x, y):
    length = (x**2 + y**2)**0.5
    if length <= 200:
        return "red"
    else:
        return "blue"


def draw_dot(x, y):
    turtle.pensize(2)
    turtle.pencolor(dot_color(x, y))
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(1)


for z in range(500):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    draw_dot(x, y)

turtle.done()
