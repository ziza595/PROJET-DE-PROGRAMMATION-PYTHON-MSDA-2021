import turtle
import dessinMSDA
import math

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
dessinMSDA.trapeze(60,40,10)

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

#bras
def bras(x,y,sens):
    if sens=="gauche":
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        dessinMSDA.rectangle(math.fabs(x)-60,y)

        turtle.penup()
        turtle.goto(x+20,y-5)
        turtle.pendown()
        dessinMSDA.rectangle(math.fabs(x)-70,y-10)

        turtle.penup()
        turtle.goto(x+30,3-y)
        turtle.left(90)
        turtle.pendown()
        dessinMSDA.rectangle(math.fabs(x)-75,y+15)

        turtle.penup()
        turtle.goto(x+32,2-y)
        turtle.right(90)
        turtle.pendown()
        dessinMSDA.rectangle(math.fabs(x)-5,y+10)
    else:
        turtle.penup()
        turtle.goto(x-20,y)
        turtle.pendown()
        dessinMSDA.rectangle(math.fabs(x)-60,y)

        turtle.penup()
        turtle.goto(x-30,y-5)
        turtle.pendown()
        dessinMSDA.rectangle(math.fabs(x)-70,y-10)

        turtle.penup()
        turtle.goto(x-66,3-y)
        turtle.left(90)
        turtle.pendown()
        dessinMSDA.rectangle(math.fabs(x)-75,y+15)

        turtle.penup()
        turtle.goto(x-65,2-y)
        turtle.right(90)
        turtle.pendown()
        dessinMSDA.rectangle(math.fabs(x)-5,y+10)
bras(105,20,"gauche")
bras(-105,20,"droite")
#oreille
def oreille(x,sens):
    if sens=="gauche":
        turtle.penup()
        turtle.goto(x,190)
        turtle.left(180)
        turtle.pendown()
        dessinMSDA.demi_cercle(20)
    else:
        turtle.penup()
        turtle.goto(x,152)
        turtle.right(90)
        turtle.pendown()
        dessinMSDA.demi_cercle(20)
oreille(-105,"gauche")
oreille(105,"droite")

#chapeau
turtle.penup()
turtle.goto(40,220)
turtle.left(180)
turtle.pendown()
dessinMSDA.demi_cercle(40)

#chaussure
def chaussure(x1,x2,sens):
    if sens=="gauche":
        turtle.penup()
        turtle.goto(x1,-240)
        turtle.left(90)
        turtle.pendown()
        dessinMSDA.rectangle(60,10)

        turtle.penup()
        turtle.goto(x2,-270)
        turtle.pendown()
        dessinMSDA.rectangle(88,30)
    else:
        turtle.penup()
        turtle.goto(x1,-240)
        turtle.pendown()
        dessinMSDA.rectangle(60,10)

        turtle.penup()
        turtle.goto(x2,-270)
        turtle.pendown()
        dessinMSDA.rectangle(88,30)
chaussure(-85,-100,"gauche")
chaussure(25,12,"droite")

#Main
turtle.penup()
turtle.goto(160,-156)
turtle.pendown()
dessinMSDA.ellipse(25)

turtle.penup()
turtle.goto(-145,-157)
turtle.right(45)
turtle.pendown()
dessinMSDA.ellipse(25)

turtle.done()
