import turtle
import math

# Bu betik extra olarak yazılmıştır. Lab Quizine Dahil Sorulardan Birisi Değildir.


def cordinate(x0, y0, v0y, v0x, t):
    x = x0 + v0x * t
    y = y0 + v0y * t - 4.9 * t**2
    return x, y


def max_point(v0y):
    return y0 + (v0**2 / (2 * 9.8))


alpha = float(input("enter alpha: "))
v0 = float(input("initial speed: "))


v0x = math.cos(math.radians(alpha)) * v0
v0y = math.sin(math.radians(alpha)) * v0

x0 = -500
y0 = 0

turtle.setup(1000, 1000)
turtle.goto(-500, 0)
turtle.goto(500, 0)
turtle.penup()
turtle.goto(x0, y0)
turtle.pendown()
y = 0
t = 0
cordinates_x = []
cordinates_y = []
while y >= 0:
    x, y = cordinate(x0, y0, v0y, v0x, t)
    cordinates_x += [x]
    cordinates_y += [y]
    t += 0.05

for x in range(len(cordinates_x)):
    turtle.goto(cordinates_x[x], cordinates_y[x])
    if x % 40 == 0:
        turtle.write("t=" + str(format(x*0.1, ".2f")))
        turtle.dot(5)
    else:
        turtle.dot(1)
    if cordinates_y[x] == max(cordinates_y):
        turtle.goto(cordinates_x[x], cordinates_y[x] / 2)
        turtle.write("hmax=" + str(cordinates_y[x]))
        turtle.goto(cordinates_x[x], 0)
        turtle.goto(cordinates_x[x], cordinates_y[x])
turtle.write(format(t, ".2f"))
turtle.dot(5)
turtle.done()
