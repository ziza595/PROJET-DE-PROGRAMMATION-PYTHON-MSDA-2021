#===================================================================#
#                   IMPORT DU MODULE TURTLE                         #
#===================================================================#

import turtle

#===================================================================#
#                   PERSONNALISATION DE L'INTERFACE                 #
#===================================================================#

turtle.title("PROJET PYTHON M1SDA AVEC TURTLE") # titre
turtle.bgcolor("skyblue") # arrière plan
turtle.pensize(2) # épaisseur de ligne


#===================================================================#
#                   DEFINITION DES FONCTIONS                        #
#===================================================================#

def cercle(rayon):
    """Objectif:

    Dessine un cercle avec un rayon donné.
    Le centre correspond aux unités de rayon à gauche de la tortue ;
    Etant donné que l'étendue n'est pas spécifiée, cette fonction 
    dessine un cercle complet.
    
    Méthode:

    Le cercle est obtenu à partir de la fonction `circle` de `turtle`
    qui utlise la méthode approximative du polygone régulier inscrit 
    avec un nombre d'étapes qui est déterminé automatiquement s'il 
    n'est pas précisé.

    Arguments:

    :param rayon: désigne le rayon du cercle
    :type rayon: int ou float
    

    Retour:

    Un cercle complet de rayon `rayon`
    
    Usage:

    `cercle(50)`
    """

    turtle.circle(rayon)


def demi_cercle(rayon):
    """Objectif:

    Dessine un demi-cercle avec un rayon donné.
    
    Méthode:

    Le demi-cercle est obtenu à partir de la fonction `circle` de 
    `turtle` qui utlise la méthode approximative du polygone régulier
    inscrit avec un nombre d'étapes qui est déterminé automatiquement
    s'il n'est pas précisé. L'argument `extent` de `circle` nous
    permet de préciser l'angle de rotation qui vaut ici `180°`

    Arguments:

    :param rayon: désigne le rayon du cercle
    :type rayon: int ou float
    

    Retour:

    Un demi-cercle complet de rayon `rayon`
    
    Usage:

    `demi-cercle(100)`
    """

    turtle.circle(rayon, 180)


def carre(cote):
    """Objectif:

    Dessine un carré de côté donné.
    
    Méthode:

    On trace le côté du carré à l'aide de la fonction `forward` de
    `turtle` puis on fait une à droite de `90°` à l'aide de la fonction `right`. On répète cela 
    `4 fois` à l'aide de la boucle `while`
    La fonction `forward 

    Arguments:

    :param cote: désigne la mesure du côté du carré
    :type cote: int ou float
    

    Retour:

    Un carré complet de rayon `rayon`
    
    Usage:

    `carre(50)`
    """

    compteur = 0
    while compteur < 4:
        turtle.forward(cote)
        turtle.right(90)
        compteur += 1


def triangle(cote):
    """Objectif:

    Dessine un carré de côté donné.
    
    Méthode:

    On trace le côté du carré à l'aide de la fonction `forward` de
    `turtle` puis on fait une à droite de `90°` à l'aide de la fonction `right`. On répète cela 
    `4 fois` à l'aide de la boucle `while`
    La fonction `forward 

    Arguments:

    :param cote: désigne la mesure du côté du carré
    :type cote: int ou float
    

    Retour:

    Un carré complet de rayon `rayon`
    
    Usage:

    `carre(50)`
    """

    compteur = 0
    while compteur < 3:
        turtle.forward(cote)
        turtle.left(120)
        compteur += 1


def rectangle(longeur, largeur):
    compteur = 0
    while compteur < 2:
        turtle.forward(longeur)
        turtle.left(90)
        turtle.forward(largeur)
        turtle.left(90)
        compteur += 1


def polygone(cote, nb_cote):
    turtle.circle(cote, steps=nb_cote)


def trapeze(grande_base, petite_base):
    turtle.forward(grande_base)
    turtle.left(120)
    turtle.forward(min(grande_base, petite_base))
    turtle.left(60)
    turtle.forward(petite_base)
    turtle.left(60)
    turtle.forward(min(grande_base, petite_base))


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

trapeze(100, 50)
turtle.done()