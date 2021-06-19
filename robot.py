import turtle
import dessinMSDA
import math

turtle.speed(20)
#tete
turtle.penup()
turtle.goto(-105,70)
turtle.pendown()
dessinMSDA.rectangle(210,150,"#b4c639")


#yeux
turtle.penup()
turtle.goto(-40,160)
turtle.pendown()
dessinMSDA.cercle(20,"white")
turtle.penup()
turtle.goto(40,160)
turtle.pendown()
dessinMSDA.cercle(20,"white")

turtle.penup()
turtle.goto(-105,120)
turtle.pendown()
turtle.forward(210)

#bouche
turtle.penup()
turtle.goto(50,120)
turtle.left(180)
turtle.pendown()
dessinMSDA.trapeze(50,30,"lightgray")

#cou
turtle.penup()
turtle.goto(-20,30)
turtle.right(180)
turtle.pendown()
dessinMSDA.rectangle(40,40,"#808080")

#ventre
turtle.penup()
turtle.goto(-105,-130)
#turtle.right(90)
turtle.pendown()
dessinMSDA.rectangle(210,160,"#b4c639")

turtle.penup()
turtle.goto(-80,-120)
turtle.pendown()
dessinMSDA.rectangle(160,140,"white")

#pied
turtle.penup()
turtle.goto(-80,-130)
turtle.right(90)
turtle.pendown()
dessinMSDA.rectangle(100,50,"#808080")

turtle.penup()
turtle.goto(30,-130)
turtle.pendown()
dessinMSDA.rectangle(100,50,"#808080")

#bras
def bras(x,y,sens):
    if sens=="gauche":
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        dessinMSDA.rectangle(math.fabs(x)-60,y,"#27a9ca")

        turtle.penup()
        turtle.goto(x+20,y-5)
        turtle.pendown()
        dessinMSDA.rectangle(math.fabs(x)-70,y-10,"#ff8226")

        turtle.penup()
        turtle.goto(x+30,1-y)
        turtle.left(90)
        turtle.pendown()
        dessinMSDA.rectangle(math.fabs(x)-75,y+15,"#b4c639")

        turtle.penup()
        turtle.goto(x+32,2-y)
        turtle.right(90)
        turtle.pendown()
        dessinMSDA.rectangle(math.fabs(x)-5,y+8,"#808080")
    else:
        turtle.penup()
        turtle.goto(x-20,y)
        turtle.pendown()
        dessinMSDA.rectangle(math.fabs(x)-60,y,"#27a9ca")

        turtle.penup()
        turtle.goto(x-30,y-5)
        turtle.pendown()
        dessinMSDA.rectangle(math.fabs(x)-70,y-10,"#ff8226")

        turtle.penup()
        turtle.goto(x-60,-y)
        turtle.left(90)
        turtle.pendown()
        dessinMSDA.rectangle(math.fabs(x)-75,y+15,"#b4c639")

        turtle.penup()
        turtle.goto(x-58,2-y)
        turtle.right(90)
        turtle.pendown()
        dessinMSDA.rectangle(math.fabs(x)-5,y+7,"#808080")
bras(105,20,"gauche")
bras(-105,20,"droite")
#oreille

#droite
turtle.penup()
turtle.goto(105,160)
turtle.left(90)
turtle.pendown()
dessinMSDA.demi_cercle(20,"#27a9ca")
#gauche
turtle.penup()
turtle.goto(-105,200)
#turtle.left(90)
turtle.pendown()
dessinMSDA.demi_cercle(20,"#27a9ca")


#chapeau
turtle.penup()
turtle.goto(40,220)
turtle.left(90)
turtle.pendown()
dessinMSDA.demi_cercle(40,"#27a9ca")

#chaussure
#gauche
turtle.penup()
turtle.goto(-85,-240)
turtle.left(90)
turtle.pendown()
dessinMSDA.rectangle(60,10,"#27a9ca")

turtle.penup()
turtle.goto(-100,-270)
turtle.pendown()
dessinMSDA.rectangle(88,30,"#27a9ca")
#droite
turtle.penup()
turtle.goto(25,-240)
turtle.pendown()
dessinMSDA.rectangle(60,10,"#27a9ca")

turtle.penup()
turtle.goto(12,-270)
turtle.pendown()
dessinMSDA.rectangle(88,30,"#27a9ca")


#Main
turtle.penup()
turtle.goto(160,-156)
turtle.pendown()
dessinMSDA.ellipse(25,"#ff8226")

turtle.penup()
turtle.goto(-140,-157)
turtle.right(45)
turtle.pendown()
dessinMSDA.ellipse(25,"#ff8226")


#yeux noir
turtle.penup()
turtle.goto(-30,165)
turtle.pendown()
dessinMSDA.cercle(10,"black")
turtle.penup()
turtle.goto(50,165)
turtle.pendown()
dessinMSDA.cercle(10,"black")

turtle.penup()
turtle.goto(1000,1000)
turtle.done()
