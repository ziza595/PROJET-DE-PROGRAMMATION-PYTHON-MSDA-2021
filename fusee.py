import turtle
import dessinMSDA


def fusee():
    """Objectif:
    Dessine une fusee avec le module `turtle`
    
    Méthode:
    Conçu à l'aide des fonctions du module `dessinMSDA`

    Besoins: 
    -

    Entrées: 
    -

    Connues: 
    -

    Sorties: 
    Une fusée

    Résultat: 
    -

    Hypothèses: importer les modules `turtle` et `dessinMSDA`
    """
    
    # deplacer le curseur
    turtle.penup()
    turtle.goto(-75, 150)
    turtle.pendown()
    # tracer le triangle d'en-tête
    dessinMSDA.triangle(150, "#a33634")
    # tracer le carré interne
    turtle.penup()
    turtle.goto(-25, 150)
    turtle.pendown()
    dessinMSDA.carre(50, "#eb928e")
    # trapèze avec rectangle interne
    turtle.penup()
    turtle.goto(-102, 86)
    turtle.pendown()
    dessinMSDA.trapeze(90, 75, "#a33634")
    # rectangle interne
    turtle.penup()
    turtle.goto(-39, 87)
    turtle.pendown()
    dessinMSDA.rectangle(75, 63, "#eb928e")
    # trapèze étendu avec rectangle interne
    turtle.penup()
    turtle.goto(-123, 66)
    turtle.pendown()
    dessinMSDA.trapeze(30, 204, "#a33634")
    # rectangle interne
    turtle.penup()
    turtle.goto(-102, 66)
    turtle.pendown()
    dessinMSDA.rectangle(204, 21, "#eb928e")
    # grand rectangle
    turtle.penup()
    turtle.goto(-123, 36)
    turtle.pendown()
    dessinMSDA.rectangle(246, 31, "#a33634")
    # rectangle interne
    turtle.penup()
    turtle.goto(-102, 36)
    turtle.pendown()
    dessinMSDA.rectangle(204, 31, "#c4c6c8")
    # triangles quelconques
    turtle.penup()
    turtle.goto(-123, 36)
    turtle.right(80)
    turtle.pendown()
    turtle.fillcolor("#a33634")
    turtle.begin_fill()
    turtle.forward(80)
    turtle.left(165)
    turtle.forward(80)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(123, 36)
    turtle.left(180)
    turtle.pendown()
    turtle.fillcolor("#a33634")
    turtle.begin_fill()
    turtle.forward(80)
    turtle.right(165)
    turtle.forward(80)
    turtle.right(100)
    turtle.end_fill()
    # cercles disjoints
    turtle.penup()
    turtle.goto(-75, -20)
    turtle.pendown()
    dessinMSDA.cercle(25, "#eb928e")

    turtle.penup()
    turtle.goto(75, -20)
    turtle.pendown()
    dessinMSDA.cercle(25, "#eb928e")
    # carré centré
    turtle.penup()
    turtle.goto(-30, -24)
    turtle.pendown()
    dessinMSDA.carre(60, "#c4c6c8")
    # avant dernier rectangle
    turtle.penup()
    turtle.goto(-70, -74)
    turtle.pendown()
    dessinMSDA.rectangle(140, 50, "#c4c6c8")
    # petit carré
    turtle.penup()
    turtle.goto(-15, -104)
    turtle.pendown()
    dessinMSDA.carre(30, "#c4c6c8")
    # dernier trapèze
    turtle.penup()
    turtle.goto(-85, -173)
    turtle.pendown()
    dessinMSDA.trapeze(100, 30, "#a33634")
    # rectangle interne
    turtle.penup()
    turtle.forward(70)
    turtle.pendown()
    dessinMSDA.rectangle(30, 70, "#c4c6c8")
    # deux petits cercles
    turtle.penup()
    turtle.goto(-30, -95)
    turtle.pendown()
    dessinMSDA.cercle(7, "#eb928e")

    turtle.penup()
    turtle.goto(30, -95)
    turtle.pendown()
    dessinMSDA.cercle(7, "#eb928e")
    # fin
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()


if __name__ == "__main__":
    fusee()
    turtle.done()