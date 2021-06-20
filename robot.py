import turtle
import dessinMSDA
import math


def robot():
    """Objectif:
    Dessine un robot avec le module `turtle`
    
    Méthode:
    Conçu à l'aide des fonctions du module `dessinMSDA`

    Besoins: 
    -

    Entrées: 
    -

    Connues: 
    -

    Sorties: 
    Un robot

    Résultat: 
    -

    Hypothèses: importer les modules `turtle`, `dessinMSDA` et `math`
    """

    #tete
    turtle.penup()
    turtle.goto(-105,70)
    turtle.pendown()
    dessinMSDA.rectangle(210,150,"#b4c639")

    # oeil gauche
    turtle.penup()
    turtle.goto(-40,160)
    turtle.pendown()
    dessinMSDA.cercle(20,"white")

    # oeil droit
    turtle.penup()
    turtle.goto(40,160)
    turtle.pendown()
    dessinMSDA.cercle(20,"white")

    # limite de la bouche
    turtle.penup()
    turtle.goto(-105,120)
    turtle.pendown()
    turtle.forward(210)

    # bouche
    turtle.penup()
    turtle.goto(50,120)
    turtle.left(180)
    turtle.pendown()
    dessinMSDA.trapeze(50,30,"darkgray")

    # cou
    turtle.penup()
    turtle.goto(-20,30)
    turtle.right(180)
    turtle.pendown()
    dessinMSDA.rectangle(40,40,"#808080")

    # ventre extérieur
    turtle.penup()
    turtle.goto(-105,-130)
    turtle.pendown()
    dessinMSDA.rectangle(210,160,"#b4c639")

    # ventre intérieur
    turtle.penup()
    turtle.goto(-80,-120)
    turtle.pendown()
    dessinMSDA.rectangle(160,140,"white")

    # pied droit
    turtle.penup()
    turtle.goto(-80,-130)
    turtle.right(90)
    turtle.pendown()
    dessinMSDA.rectangle(100,50,"#808080")

    # pied gauche
    turtle.penup()
    turtle.goto(30,-130)
    turtle.pendown()
    dessinMSDA.rectangle(100,50,"#808080")

    # bras gauche
    turtle.penup()
    turtle.goto(105,20)
    turtle.pendown()
    dessinMSDA.rectangle(math.fabs(105)-60,20,"#27a9ca")

    turtle.penup()
    turtle.goto(105+20,20-5)
    turtle.pendown()
    dessinMSDA.rectangle(math.fabs(105)-70,20-10,"#ff8226")

    turtle.penup()
    turtle.goto(105+30,1-20)
    turtle.left(90)
    turtle.pendown()
    dessinMSDA.rectangle(math.fabs(105)-75,20+15,"#b4c639")

    turtle.penup()
    turtle.goto(105+32,2-20)
    turtle.right(90)
    turtle.pendown()
    dessinMSDA.rectangle(math.fabs(105)-5,20+8,"#808080")

    # bras droit
    turtle.penup()
    turtle.goto(-105-20,20)
    turtle.pendown()
    dessinMSDA.rectangle(math.fabs(-105)-60,20,"#27a9ca")

    turtle.penup()
    turtle.goto(-105-30,20-5)
    turtle.pendown()
    dessinMSDA.rectangle(math.fabs(-105)-70,20-10,"#ff8226")

    turtle.penup()
    turtle.goto(-105-60,-20)
    turtle.left(90)
    turtle.pendown()
    dessinMSDA.rectangle(math.fabs(-105)-75,20+15,"#b4c639")

    turtle.penup()
    turtle.goto(-105-58,2-20)
    turtle.right(90)
    turtle.pendown()
    dessinMSDA.rectangle(math.fabs(-105)-5,20+7,"#808080")

    # oreille droit
    turtle.penup()
    turtle.goto(105,160)
    turtle.left(90)
    turtle.pendown()
    dessinMSDA.demi_cercle(20,"#27a9ca")

    # oreille gauche
    turtle.penup()
    turtle.goto(-105,200)
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
    dessinMSDA.cercle(12,"black")
    turtle.penup()
    turtle.goto(50,165)
    turtle.pendown()
    dessinMSDA.cercle(12,"black")

    # text du ventre
    turtle.penup()
    turtle.goto(-50,-40)
    turtle.pendown()
    turtle.color("green")
    turtle.write("Created By", align="left", font=("Verdana", 12))

    turtle.penup()
    turtle.goto(-50,-70)
    turtle.pendown()
    turtle.color("green")
    turtle.write("AAB & KY", move=True, align="left", font=("Verdana", 15))
    # fin
    turtle.penup()
    turtle.goto(-8,-90)
    turtle.pendown()


if __name__ == "__main__":
    robot()
    turtle.done()
