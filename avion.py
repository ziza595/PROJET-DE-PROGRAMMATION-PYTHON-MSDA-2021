import turtle
import dessinMSDA




turtle.color("blue")
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.penup()
turtle.goto(92,130)
turtle.pendown()
dessinMSDA.cercle(18)
turtle.end_fill()

#grande aile
turtle.fillcolor('blue')
turtle.color("blue")
turtle.begin_fill()
turtle.penup()
turtle.goto(-116,-50)
turtle.right(69)
turtle.pendown()
dessinMSDA.polygone(120,5)
turtle.end_fill()

turtle.color("white")
turtle.fillcolor('white')
turtle.begin_fill()
turtle.penup()
turtle.goto(-110,45)
turtle.right(70)
turtle.pendown()
dessinMSDA.polygone(120,5)
turtle.end_fill()


turtle.color("blue")
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.penup()
turtle.goto(73,153)
turtle.left(14)
turtle.pendown()
dessinMSDA.rectangle(230,35)
turtle.end_fill()

#petite aile
turtle.fillcolor('blue')
turtle.color("blue")
turtle.begin_fill()
turtle.penup()
turtle.goto(-40,-25)
turtle.right(90)
turtle.pendown()
dessinMSDA.polygone(60,5)
turtle.end_fill()

turtle.color("white")
turtle.fillcolor('white')
turtle.begin_fill()
turtle.penup()
turtle.goto(-45,-130)
turtle.right(79)
turtle.pendown()
dessinMSDA.polygone(60,5)
turtle.end_fill()

# turtle.color("white")
# turtle.fillcolor('white')
# turtle.begin_fill()
# turtle.penup()
# turtle.goto(-82,-45)
# turtle.right(30)
# turtle.pendown()
# dessinMSDA.polygone(22,6)
# turtle.end_fill()

turtle.done()