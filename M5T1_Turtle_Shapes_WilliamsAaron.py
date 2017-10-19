#CTI-110
#Shape Drawer
#Aaron Williams
#10/19/2017
#This program uses the turtle module to draw a square and a triangle

#Sets the appearance of the window and the two turtles
import turtle
win = turtle.Screen()
win.bgcolor('skyblue')
triangle = turtle.Turtle()
square = turtle.Turtle()
triangle.pencolor('red')
square.pencolor('purple')
triangle.pensize('3')
square.pensize('3')

#Moves the triangle turtle into position
triangle.penup()
triangle.backward(200)
triangle.pendown()

#Draws the square
for i in range(4):
    square.forward(100)
    square.left(90)

#Draws the triangle
for i in range(3):
    triangle.forward(100)
    triangle.left(120)
    

win.mainloop()
