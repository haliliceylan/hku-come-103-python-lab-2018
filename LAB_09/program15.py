import turtle


def gotoSafe(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()


def drawCircle(x, y, radius):
    gotoSafe(x, y)
    turtle.circle(radius)


def drawArms():
    gotoSafe(-50, 110)
    # left arm
    turtle.setheading(180)
    turtle.forward(50)
    turtle.right(75)
    turtle.forward(50)
    turtle.left(45)
    turtle.forward(10)
    turtle.right(180)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    # right arm
    gotoSafe(50, 110)
    turtle.left(20)
    turtle.forward(50)
    turtle.left(45)
    turtle.forward(10)
    turtle.right(180)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)


def drawBase():
    drawCircle(0, -100, 80)


def drawMidSection():
    drawCircle(0, 60, 50)


def drawHead():
    drawCircle(0, 160, 30)
    drawCircle(-10, 190, 5)
    drawCircle(10, 190, 5)
    gotoSafe(-15, 175)
    turtle.forward(33)


def drawHat():
    gotoSafe(-45, 200)
    turtle.begin_fill()
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.end_fill()
    pass


turtle.speed(0)

drawBase()
drawMidSection()
drawHead()
drawArms()
drawHat()

turtle.hideturtle()
turtle.done()
