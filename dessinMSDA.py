#===================================================================#
#                   IMPORT DU MODULE TURTLE                         #
#===================================================================#

from turtle import *
from math import sqrt

#===================================================================#
#                   PERSONNALISATION DE L'INTERFACE                 #
#===================================================================#

title("PROJET DE PROGRAMMATION PYTHON :-) Turtle | MSDA")
shape("turtle")
pencolor("#aaa")


#===================================================================#
#                   DEFINITION DES FONCTIONS                        #
#===================================================================#

def cercle(rayon, couleur):
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

    fillcolor(couleur)
    begin_fill()
    circle(rayon)
    end_fill()


def demi_cercle(rayon, couleur):
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

    fillcolor(couleur)
    begin_fill()
    circle(rayon, 180)
    end_fill()


def carre(longueur, couleur):
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

    fillcolor(couleur)
    begin_fill()
    for i in range(4):
        forward(longueur)
        left(90)
    end_fill()


def triangle(longueur, couleur):
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

    fillcolor(couleur)
    begin_fill()
    forward(longueur)
    left(135)
    forward(longueur / sqrt(2))
    left(90)
    forward(longueur / sqrt(2))
    left(135)
    end_fill()


def rectangle(largeur, hauteur, couleur):
    fillcolor(couleur)
    begin_fill()
    for i in range(2):
        forward(largeur)
        left(90)
        forward(hauteur)
        left(90)
    end_fill()


def polygone(cote, nb_cote):
    turtle.circle(cote, steps=nb_cote)


def trapeze(longueur, pb, couleur):
    fillcolor(couleur)
    begin_fill()
    forward(longueur / sqrt(2))
    forward(pb)
    forward(longueur / sqrt(2))
    left(135)
    forward(longueur)
    left(45)
    forward(pb)
    left(45)
    forward(longueur)
    left(135)
    end_fill()


def losange(longueur, couleur):
    fillcolor(couleur)
    begin_fill()
    left(120)
    forward(longueur)
    left(120)
    forward(longueur)
    left(60)
    forward(longueur)
    left(120)
    forward(longueur)
    end_fill()

def ellipse(rayon, couleur):
    fillcolor(couleur)
    begin_fill()
    left(45)
    compteur = 0
    while compteur < 2:
        circle(rayon, 90)
        circle(rayon/2, 90)
        compteur += 1
    end_fill()
