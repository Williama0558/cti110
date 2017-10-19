#CTI-110
#Initial Writer
#Aaron Williams
#10/19/2017
#This program uses the turtle module to write my initials

#Sets the appearance of the window and the two turtles
import turtle
win = turtle.Screen()
win.bgcolor('blue')
aaron = turtle.Turtle()
williams = turtle.Turtle()
aaron.pencolor('red')
williams.pencolor('red')
aaron.pensize('3')
williams.pensize('3')

#Gets the aaron turtle into position
aaron.penup()
aaron.backward(200)
aaron.pendown()

#Writes the A
aaron.left(70)
aaron.forward(100)
aaron.right(140)
aaron.forward(100)
aaron.backward(50)
aaron.right(110)
aaron.forward(39)

#Gets the williams turtle into position
williams.penup()
williams.left(90)
williams.forward(100)
williams.pendown()

#Writes the W
williams.right(160)
williams.forward(100)
williams.left(140)
williams.forward(100)
williams.right(140)
williams.forward(100)
williams.left(140)
williams.forward(100)

win.mainloop()
