import turtle
import dessinMSDA as d

# triangle du sommet
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
d.triangle(100)

# carrée intérieur
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.left(90)
d.carre(47)

# trapèze contenant un carré
turtle.penup()
turtle.goto(39, -37)
turtle.left(270)
turtle.pendown()
d.trapeze(100, 76, 20)

# rectangle interieur
turtle.penup()
turtle.forward(25)
turtle.left(90)
turtle.pendown()
d.rectangle(87, 76)

# grand trapèze
turtle.penup()
turtle.goto(-50, -63)
turtle.left(-90)
turtle.pendown()
turtle.forward(204) #
turtle.left(120)
turtle.forward(30) #
turtle.left(60)
turtle.forward(200)
turtle.left(60)
turtle.forward(30)

# barres verticales
turtle.penup()
turtle.left(120)
turtle.forward(15)
turtle.pendown()
turtle.left(90)
turtle.forward(30)
turtle.penup()
turtle.right(90)
turtle.forward(144)
turtle.right(90)
turtle.pendown()
turtle.forward(30)

# fermer la boucle
turtle.done()