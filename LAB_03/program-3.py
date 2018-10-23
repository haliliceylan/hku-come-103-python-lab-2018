import turtle

# draw left yellow circle
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

# go right side of circle
turtle.penup()
turtle.goto(25,25)
turtle.pendown()

# draw right red triagle
turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(25,75)
turtle.goto(75,25)
turtle.goto(25,-25)
turtle.goto(25,25)
turtle.end_fill()

#go right side for right triangle

turtle.penup()
turtle.goto(75,25)
turtle.pendown()

#draw right blue triagle

turtle.fillcolor("blue")
turtle.begin_fill()
turtle.goto(125,75)
turtle.goto(125,-25)
turtle.goto(75,25)
turtle.end_fill()


# goto left corner of square
turtle.penup()
turtle.goto(25,75)
turtle.pendown()

# draw square
turtle.goto(125,75)
turtle.goto(125,-25)
turtle.goto(25,-25)
turtle.goto(25,75)

# goto middle point of right side of blue triangle

turtle.penup()
turtle.goto(125,25)
turtle.pendown()

#draw right circle

turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.setheading(270)
turtle.circle(25)
turtle.end_fill()

turtle.done()