import turtle
import dessinMSDA as d

# test
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
d.triangle(100)

turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.left(90)
turtle.forward(47)
turtle.left(-90)
turtle.forward(47)
turtle.left(-90)
turtle.forward(47)

turtle.penup()
turtle.goto(39, -37)
turtle.left(90)
turtle.pendown()
d.trapeze(100, 76)

turtle.penup()
turtle.forward(25)
turtle.left(90)
turtle.pendown()
turtle.forward(87)
turtle.left(90)
turtle.forward(76)
turtle.left(90)
turtle.forward(87)

# fermer la boucle
turtle.done()