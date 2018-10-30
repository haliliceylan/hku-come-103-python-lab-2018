import turtle


variable_one = 100

#draw up green triangle
turtle.fillcolor("green")
turtle.begin_fill()
turtle.goto(variable_one,variable_one)
turtle.goto(-variable_one,variable_one)
turtle.goto(0,0)
turtle.end_fill()

#write up text yellow
turtle.penup()
turtle.goto(0,variable_one)
turtle.pencolor("green")
turtle.write("TOP",align="center")
turtle.goto(0,0)
turtle.pendown()
turtle.pencolor("black")

#draw down blue triangle
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.goto(variable_one,-variable_one)
turtle.goto(-variable_one,-variable_one)
turtle.goto(0,0)
turtle.end_fill()

#write bottom text blue
turtle.penup()
turtle.goto(0,-(variable_one + 15))
turtle.pencolor("blue")
turtle.write("BOTTOM",align="center")
turtle.goto(0,0)
turtle.pendown()
turtle.pencolor("black")

#draw left yellow sqaure
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.goto(-variable_one,variable_one)
turtle.goto(-variable_one*2,0)
turtle.goto(-variable_one,-variable_one)
turtle.goto(0,0)
turtle.end_fill()

#write left text yellow

turtle.penup()
turtle.goto(-(variable_one*2 + 20),0-(8))
turtle.pencolor("yellow")
turtle.write("LEFT",align="center")
turtle.goto(0,0)
turtle.pendown()
turtle.pencolor("black")

#draw right red sqaure
turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(variable_one,variable_one)
turtle.goto(variable_one*2,0)
turtle.goto(variable_one,-variable_one)
turtle.goto(0,0)
turtle.end_fill()

#write right text red

turtle.penup()
turtle.goto((variable_one*2 + 20),0-(8))
turtle.pencolor("red")
turtle.write("RIGHT",align="center")
turtle.goto(0,0)
turtle.pendown()
turtle.pencolor("black")

# draw left square

turtle.penup()
turtle.goto(variable_one/2,0)
turtle.setheading(270)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(variable_one/2)
turtle.end_fill()


# draw left square

turtle.penup()
turtle.goto(-variable_one/2,0)
turtle.setheading(90)
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(variable_one/2)
turtle.end_fill()

turtle.done()
