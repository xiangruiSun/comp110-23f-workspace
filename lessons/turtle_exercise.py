"""Turtle."""

from turtle import Turtle, colormode, done

colormode(255)
#this is needed for .color method to function

leo: Turtle = Turtle()
leo.color(255, 0, 0)
leo.speed(2)

leo.begin_fill()
leo.penup()
leo.goto(45, 60)
leo.pendown()
i: int = 0
side_length: int = 300
while i < 3:
    leo.forward(side_length)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()
bob.color(0, 0, 0)
bob.penup()
bob.goto(45, 60)
bob.pendown()
i: int = 0
while i < 10:
    side_length = side_length * 0.9
    bob.forward(side_length)
    bob.left(120)
    i += 1

done()