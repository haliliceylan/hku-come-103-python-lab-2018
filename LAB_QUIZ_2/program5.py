import turtle


turtle.pensize(2)
turtle.goto(-200, 0)
turtle.goto(200, 0)
turtle.goto(200, -200)
turtle.goto(-200, -200)
turtle.goto(-200, 0)

a = 70
b = 50
turtle.goto(-200 + a, 0 + b)

turtle.goto(200 + a, 0 + b)
turtle.goto(200, 0)
turtle.goto(200 + a, 0 + b)

turtle.goto(200 + a, -200 + b)
turtle.goto(200, -200)
turtle.goto(200 + a, -200 + b)


turtle.goto(-200 + a, -200 + b)
turtle.goto(-200, -200)
turtle.goto(-200 + a, -200 + b)

turtle.goto(-200 + a, 0 + b)
turtle.goto(-200, 0)
turtle.goto(-200 + a, 0 + b)

turtle.done()
