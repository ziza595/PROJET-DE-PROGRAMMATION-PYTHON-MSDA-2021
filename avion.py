from turtle import *
import dessinMSDA


def avion():
    """Affiche la figure représentant l'avion"""
    # deplacer le curseur
    penup()
    goto(100, 50)
    left(45)
    pendown()
    dessinMSDA.rectangle(150, 70, "green")
    right(45)
    # demi-cercle
    penup()
    left(45)
    forward(150)
    pendown()
    dessinMSDA.demi_cercle(35, "green")
    # deuxième rectangle
    penup()
    forward(150)
    pendown()
    dessinMSDA.rectangle(100, 70, "yellow")
    # aile gauche
    penup()
    right(70)
    pendown()
    fillcolor("red")
    begin_fill()
    forward(170)
    left(70)
    forward(60)
    left(97)
    forward(160)
    right(97)
    end_fill()
    # troisième rectangle
    dessinMSDA.rectangle(100, 70, "yellow")
    # queue gauche
    penup()
    forward(100)
    right(70)
    pendown()
    fillcolor("red")
    begin_fill()
    forward(80)
    left(70)
    forward(60)
    left(100)
    forward(105)
    end_fill()
    # queue droite
    penup()
    right(30)
    pendown()
    fillcolor("red")
    begin_fill()
    forward(80)
    left(70)
    forward(60)
    left(95)
    forward(90)
    left(35)
    forward(70)
    end_fill()
    # aile droite
    penup()
    right(90)
    forward(200)
    right(93)
    forward(72)
    right(10)
    pendown()
    fillcolor("red")
    begin_fill()
    forward(170)
    right(70)
    forward(60)
    right(97)
    forward(171)
    end_fill()
    # étoile
    penup()
    goto(35, 25)
    right(100)
    pendown()
    fillcolor("green")
    begin_fill()
    alpha = 180 - 180/5
    for i in range(5):
        forward(15)
        right(alpha - 360/5)
        forward(15)
        left(alpha)
    end_fill()
    # fin
    penup()
    goto(0, -200)
    left(60)
    pendown()


if __name__ == "__main__":
    avion()
    done()