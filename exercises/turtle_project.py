"""A landscope of beautiful forest."""
 
__author__ = "730525294"
 
from turtle import Turtle, done
from random import randint


def main() -> None:
    """Draw a forest of three beautiful trees."""
    a_turtle: Turtle = Turtle()
    a_turtle.hideturtle()
    a_turtle.speed(200)

    i: int = 0
    i1: int = 0

    moon(a_turtle, 300, 240)

    while i1 < 10:
        a: int = 200 - 40 * randint(-1, 3)
        star(a_turtle, 300 - 70 * i1, a)
        i1 += 1

    while i < 3:
        tree_base(a_turtle, 101 - i * 150, -142.0, 50)
        tree_top(a_turtle, 65 - i * 150, -90)
        i += 1
    

def tree_base(turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a tree of given width at position x, y."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("Brown") 
    turtle.begin_fill()
    i: int = 0
    while i < 4:
        turtle.forward(width) 
        turtle.left(90)
        i += 1 
    turtle.end_fill()


def triangle(turtle: Turtle, length: float) -> None:
    """This is a helper function to draw a triangle with a given length."""
    turtle.fillcolor("lightgreen") 
    turtle.begin_fill() 
    turtle.forward(length) 
    turtle.left(135) 
    turtle.forward(length / 1.44) 
    turtle.left(90) 
    turtle.forward(length / 1.44) 
    turtle.left(135) 
    turtle.end_fill()


def tree_top(turtle: Turtle, x: float, y: float) -> None:
    """Draw a tree top at x,y using triangle function."""
    i: int = 0
    while i < 3:
        turtle.penup() 
        turtle.goto(x + i * 14, y + i * 40) 
        turtle.pendown() 
        triangle(turtle, 120 - i * 30)
        i += 1


def star(turtle: Turtle, x: float, y: float) -> None:
    """Draw a yellow star at x, y.""" 
    i: int = 0
    turtle.pencolor("yellow")
    turtle.penup() 
    turtle.goto(x, y)
    turtle.pendown()

    while i < 5:
        turtle.forward(20)
        turtle.right(144)
        i += 1
    turtle.pencolor("black")


def moon(turtle: Turtle, x: float, y: float) -> None:
    """Draw a moon at x, y."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("grey")
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()


if __name__ == "__main__":
    main()
    done()