import turtle


def cercle(rayon):
    turtle.circle(rayon)


def demi_cercle(rayon):
    turtle.left(90)
    turtle.circle(rayon, 180)


def carre(cote):
    compteur = 0
    while compteur < 4:
        turtle.forward(cote)
        turtle.right(90)
        compteur += 1


def triangle(cote):
    compteur = 0
    while compteur < 3:
        turtle.forward(cote)
        turtle.left(120)
        compteur += 1


def rectangle(longeur, largeur):
    compteur = 0
    while compteur < 2:
        turtle.forward(max(longeur, largeur))
        turtle.left(90)
        turtle.forward(min(longeur, largeur))
        turtle.left(90)
        compteur += 1


def polygone(cote, nb_cote):
    turtle.circle(cote, steps=nb_cote)


def trapeze(grande_base, petite_base):
    turtle.forward(max(grande_base, petite_base))
    turtle.left(120)
    turtle.forward(min(grande_base, petite_base))
    turtle.left(60)
    turtle.forward(min(grande_base, petite_base))
    turtle.left(60)
    turtle.forward(min(grande_base, petite_base))
    # turtle.left(120)
    # turtle.forward(max(grande_base, petite_base))


def losange(cote):
    turtle.left(120)
    turtle.forward(cote)
    turtle.left(120)
    turtle.forward(cote)
    turtle.left(60)
    turtle.forward(cote)
    turtle.left(120)
    turtle.forward(cote)

def ellipse(rayon):
    turtle.left(45)
    compteur = 0
    while compteur < 2:
        turtle.circle(rayon, 90)
        turtle.circle(rayon/2, 90)
        compteur += 1

# personnalisation de l'interface
turtle.title("PROJET PYTHON M1SDA AVEC TURTLE")
turtle.bgcolor("skyblue")
# turtle.pensize(2)
turtle.speed(10)

# fermer la boucle
