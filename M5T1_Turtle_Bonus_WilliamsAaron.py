#CTI-110
#Snowflake Drawer
#Aaron Williams
#10/19/2017
#This program uses the turtle module to draw snowflakes

#Defines the appearance of the window and the turtle.
import turtle
win = turtle.Screen()
win.bgcolor('blue')
snowflake = turtle.Turtle()
snowflake.pencolor('white')
snowflake.pensize('3')

#Creates the polygon shape.
for i in range(9):
    snowflake.forward(100)
    snowflake.left(40)

#Adds the flakes to the shape.
for i in range(9):
    snowflake.right(110)
    snowflake.forward(100)
    #Creates the line in the middle of the flake.
    snowflake.backward(50)
    snowflake.left(90)
    snowflake.forward(50)
    snowflake.backward(100)
    snowflake.forward(50)
    #Moves the turtle back to the origin of the flake.
    snowflake.left(90)
    snowflake.forward(50)
    snowflake.right(70)
    #Moves the turtle to the next point of the polygon to make another flake.
    snowflake.forward(100)
    snowflake.left(40)

win.mainloop()
    
