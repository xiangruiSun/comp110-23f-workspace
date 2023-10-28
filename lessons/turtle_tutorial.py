"""Turtle."""

from turtle import Turtle, colormode, done

colormode(255)
#this is needed for .color method to function

leo: Turtle = Turtle()

#left,right controls 乌龟的朝向
#the angle of right/left is the angle starts from the forward line

leo.color(255, 0, 0)
#<turtlevariable>.color(<red>, <green>, <blue>)
#the max amount for each color is from 0 to 255
#all 0s is black, all 255s is white

leo.penup()
leo.goto(45, 60)
leo.pendown()
#move leo to new position without drawing its path
leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(30)
    leo.right(120)
    i += 1
leo.end_fill()
#.begin_fill() .end_fill() make sure the drawing area is filled

leo.pencolor("pink") #set only pen color
leo.fillcolor(32, 67, 93) #set only fill color
leo.color("green")

leo.speed(50) #speed 
leo.hideturtle() #hide the turle
done()