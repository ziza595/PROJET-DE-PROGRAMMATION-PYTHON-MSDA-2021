import turtle
import dessinMSDA


def avion():
    """Objectif:
    Dessine un avion avec le module `turtle`
    
    Méthode:
    Conçu à l'aide des fonctions du module `dessinMSDA`

    Besoins: 
    -

    Entrées: 
    -

    Connues: 
    -

    Sorties: 
    Un avion

    Résultat: 
    -

    Hypothèses: importer les modules `turtle` et `dessinMSDA`
    """

    # deplacer le curseur
    turtle.penup()
    turtle.goto(100, 50)
    turtle.left(45)
    turtle.pendown()
    dessinMSDA.rectangle(150, 70, "green")
    turtle.right(45)
    # demi-cercle
    turtle.penup()
    turtle.left(45)
    turtle.forward(150)
    turtle.pendown()
    dessinMSDA.demi_cercle(35, "green")
    # deuxième rectangle
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()
    dessinMSDA.rectangle(100, 70, "yellow")
    # aile gauche
    turtle.penup()
    turtle.right(70)
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.forward(170)
    turtle.left(70)
    turtle.forward(60)
    turtle.left(97)
    turtle.forward(160)
    turtle.right(97)
    turtle.end_fill()
    # troisième rectangle
    dessinMSDA.rectangle(100, 70, "yellow")
    # queue gauche
    turtle.penup()
    turtle.forward(100)
    turtle.right(70)
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.forward(80)
    turtle.left(70)
    turtle.forward(60)
    turtle.left(100)
    turtle.forward(105)
    turtle.end_fill()
    # queue droite
    turtle.penup()
    turtle.right(30)
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.forward(80)
    turtle.left(70)
    turtle.forward(60)
    turtle.left(95)
    turtle.forward(90)
    turtle.left(35)
    turtle.forward(70)
    turtle.end_fill()
    # aile droite
    turtle.penup()
    turtle.right(90)
    turtle.forward(200)
    turtle.right(93)
    turtle.forward(72)
    turtle.right(10)
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.forward(170)
    turtle.right(70)
    turtle.forward(60)
    turtle.right(97)
    turtle.forward(171)
    turtle.end_fill()
    # étoile
    turtle.penup()
    turtle.goto(35, 25)
    turtle.right(100)
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    alpha = 180 - 180/5
    for i in range(5):
        turtle.forward(15)
        turtle.right(alpha - 360/5)
        turtle.forward(15)
        turtle.left(alpha)
    turtle.end_fill()
    # fin
    turtle.penup()
    turtle.goto(0, -200)
    turtle.left(60)
    turtle.pendown()


if __name__ == "__main__":
    avion()
    turtle.done()