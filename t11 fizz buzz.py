# day 40 GitHub atlemgw

import turtle

t = turtle

for i in range(360):
    t.fd(i)
    t.left(90)
    t.speed(10)
    if i % 3 == 0 and i % 5 == 0:
        t.right(3)
        t.fd(i + 0.15)
    if i % 3 == 0:
        t.right(1)
        t.fd(i * 0.6)
    if i % 5 == 0:
        t.left(2)
        t.fd( i * 0.3)