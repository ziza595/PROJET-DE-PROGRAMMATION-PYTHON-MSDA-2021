import turtle
import math


turtle.color("skyblue")
turtle.bgcolor("gray")

# rectangle
def rectangle(longeur, largeur):
    compteur = 0
    while compteur < 2:
        turtle.forward(max(longeur, largeur))
        turtle.left(90)
        turtle.forward(min(longeur, largeur))
        turtle.left(90)
        compteur += 1

# trapeze rectangle
def trapeze_rect(gbase, pbase, haut, sens):
    hyp = 200
    if sens == "gauche":
        turtle.forward(gbase)
        turtle.left(120) # 150
        turtle.forward(hyp)
        turtle.left(60)
        turtle.forward(pbase)
        turtle.left(96)
        turtle.forward(haut)
    else:
        turtle.forward(gbase)
        turtle.right(120) # 150
        turtle.forward(hyp)
        turtle.right(60)
        turtle.forward(pbase)
        turtle.right(96)
        turtle.forward(haut)
    

turtle.begin_fill()
turtle.fillcolor("lightblue")
# rectangle1
turtle.penup()
turtle.left(30)
turtle.pendown()
rectangle(150, 80)
pos1 = turtle.position()
turtle.end_fill()

turtle.begin_fill()
turtle.fillcolor("lightblue")
# demi-cercle
turtle.penup()
turtle.forward(150)
turtle.pendown()
turtle.circle(40, 180)
turtle.end_fill()

# rectangle2
turtle.begin_fill()
turtle.fillcolor("lightblue")
turtle.penup()
turtle.goto(pos1)
turtle.right(90)
turtle.forward(80)
turtle.left(90)
turtle.pendown()
rectangle(130, 80)
turtle.end_fill()

# rectangle3
turtle.begin_fill()
turtle.fillcolor("lightblue")
turtle.penup()
turtle.forward(130)
turtle.pendown()
rectangle(130, 80)
pos2 = turtle.position()

# queue
turtle.penup()
turtle.forward(130)
turtle.end_fill()
turtle.right(60)
turtle.pendown()
turtle.forward(80)

turtle.penup()
turtle.left(60)
turtle.pendown()
turtle.forward(60)

turtle.penup()
turtle.left(115)
turtle.pendown()
turtle.forward(120)
turtle.right(50)
turtle.forward(120)
turtle.left(115)
turtle.forward(60)
turtle.left(60)
turtle.forward(80)
turtle.end_fill()

# ailes
turtle.begin_fill()
turtle.fillcolor("lightblue")
turtle.penup()
turtle.goto(pos2)
turtle.right(60)
turtle.pendown()
trapeze_rect(130, 50, 172, "gauche")
turtle.end_fill()

turtle.begin_fill()
turtle.fillcolor("lightblue")
turtle.penup()
turtle.goto(pos1)
turtle.right(96)
turtle.forward(130)
turtle.left(180)
turtle.pendown()
trapeze_rect(130, 50, 172, "droite")
turtle.end_fill()

turtle.penup()
turtle.goto(1000, 1000)
turtle.pendown()


turtle.done()