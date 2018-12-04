import turtle


def main():
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    x3 = int(input("x3: "))
    y3 = int(input("y3: "))
    color = input("color: ")
    triangle(x1, y1, x2, y2, x3, y3, color)


def triangle(x1, y1, x2, y2, x3, y3, color):
    # go to start point
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.showturtle()
    turtle.pencolor(color)
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)


main()
