import turtle

# turtle setup
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# turtle move
t.penup()
t.goto(0, -300)
t.pendown()

# magic

for i in range(10):
    t.circle(i * 30)

# end
turtle.exitonclick()