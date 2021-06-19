from turtle import *
import dessinMSDA


def fusil():
    # deplacer le curseur
    penup()
    goto(-75, 150)
    pendown()
    # tracer le triangle d'en-tête
    dessinMSDA.triangle(150, "#a33634")
    # tracer le carré interne
    penup()
    goto(-25, 150)
    pendown()
    dessinMSDA.carre(50, "#eb928e")
    # trapèze avec rectangle interne
    penup()
    goto(-102, 86)
    pendown()
    dessinMSDA.trapeze(90, 75, "#a33634")
    # rectangle interne
    penup()
    goto(-39, 87)
    pendown()
    dessinMSDA.rectangle(75, 63, "#eb928e")
    # trapèze étendu avec rectangle interne
    penup()
    goto(-123, 66)
    pendown()
    dessinMSDA.trapeze(30, 204, "#a33634")
    # rectangle interne
    penup()
    goto(-102, 66)
    pendown()
    dessinMSDA.rectangle(204, 21, "#eb928e")
    # grand rectangle
    penup()
    goto(-123, 36)
    pendown()
    dessinMSDA.rectangle(246, 31, "#a33634")
    # rectangle interne
    penup()
    goto(-102, 36)
    pendown()
    dessinMSDA.rectangle(204, 31, "#c4c6c8")
    # triangles quelconques
    penup()
    goto(-123, 36)
    right(80)
    pendown()
    fillcolor("#a33634")
    begin_fill()
    forward(80)
    left(165)
    forward(80)
    end_fill()

    penup()
    goto(123, 36)
    left(180)
    pendown()
    fillcolor("#a33634")
    begin_fill()
    forward(80)
    right(165)
    forward(80)
    right(100)
    end_fill()
    # cercles disjoints
    penup()
    goto(-75, -20)
    pendown()
    dessinMSDA.cercle(25, "#eb928e")

    penup()
    goto(75, -20)
    pendown()
    dessinMSDA.cercle(25, "#eb928e")
    # carré centré
    penup()
    goto(-30, -24)
    pendown()
    dessinMSDA.carre(60, "#c4c6c8")
    # avant dernier rectangle
    penup()
    goto(-70, -74)
    pendown()
    dessinMSDA.rectangle(140, 50, "#c4c6c8")
    # petit carré
    penup()
    goto(-15, -104)
    pendown()
    dessinMSDA.carre(30, "#c4c6c8")
    # dernier trapèze
    penup()
    goto(-85, -173)
    pendown()
    dessinMSDA.trapeze(100, 30, "#a33634")
    # rectangle interne
    penup()
    forward(70)
    pendown()
    dessinMSDA.rectangle(30, 70, "#c4c6c8")
    # deux petits cercles
    penup()
    goto(-30, -95)
    pendown()
    dessinMSDA.cercle(7, "#eb928e")

    penup()
    goto(30, -95)
    pendown()
    dessinMSDA.cercle(7, "#eb928e")
    # fin
    penup()
    goto(0, -200)
    pendown()


if __name__ == "__main__":
    fusil()
    done()