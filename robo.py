import turtle
import dessinMSDA


#tete
turtle.penup()
turtle.goto(-105,70)
turtle.pendown()
dessinMSDA.rectangle(210,150)
#yeux
turtle.penup()
turtle.goto(-40,160)
turtle.pendown()
dessinMSDA.cercle(20)
turtle.penup()
turtle.goto(40,160)
turtle.pendown()
dessinMSDA.cercle(20)

turtle.penup()
turtle.goto(-105,120)
turtle.pendown()
turtle.forward(210)

turtle.penup()
turtle.goto(20,120)
turtle.left(180)
turtle.pendown()
dessinMSDA.trapeze(60,40)

#cou
turtle.penup()
turtle.goto(-20,70)
turtle.right(150)
turtle.pendown()
dessinMSDA.rectangle(40,40)

#ventre
turtle.penup()
turtle.goto(-105,-130)
turtle.left(90)
turtle.pendown()
dessinMSDA.rectangle(210,160)

#pied
turtle.penup()
turtle.goto(-80,-130)
turtle.right(90)
turtle.pendown()
dessinMSDA.rectangle(100,50)

turtle.penup()
turtle.goto(30,-130)
turtle.pendown()
dessinMSDA.rectangle(100,50)

turtle.done()
