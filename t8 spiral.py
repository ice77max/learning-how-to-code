import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)


r = 10 #radius

for i in range(300):
    t.circle(r + i, 50)

turtle.exitonclick() # exit 