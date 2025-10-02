import turtle
import time

# setup
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# functions

def zero_out_turtle():
    t.penup
    t.goto(0,0)
    t.pendown()
    t.clear()
    t.setheading(0)

def flower(repetitions, angle):
    for i in range(repetitions):
        t.fd(i)
        t.left(90)
        t.fd(i)
        t.left(90)
        t.fd(i / 2)
        t.right(angle)

# magic

for i in range(3, 20):
    flower(200, i * 10)
    time.sleep(1)
    zero_out_turtle()

# patterns I like

# flower(150, 150)
# time.sleep(2)
# zero_out_turtle()
# flower(250, 100)

turtle.exitonclick() # end