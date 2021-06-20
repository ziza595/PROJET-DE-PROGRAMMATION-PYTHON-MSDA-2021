# ===================================================================#
#                   IMPORT DU MODULE TURTLE                          #
# ===================================================================#

from turtle import *
from math import sqrt

# ===================================================================#
#                   PERSONNALISATION DE L'INTERFACE                  #
# ===================================================================#

title("PROJET DE PROGRAMMATION PYTHON :-) Turtle | MSDA")
shape("turtle")
pencolor("#aaa")


# ===================================================================#
#                   DEFINITION DES FONCTIONS                         #
# ===================================================================#


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
    :type rayon: entier ou réel
    :param couleur: désigne le remplissage du cercle
    :type couleur: chaîne de caractère


    Retour:

    Un cercle complet de rayon `rayon`
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
    :type rayon: entier ou réel
    :param couleur: désigne le remplissage du demi-cercle
    :type couleur: int ou float


    Retour:

    Un demi-cercle complet de rayon `longueur`
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
    `turtle` puis on fait une rotation à droite de `90°` à l'aide de
    la fonction `right`. On répète cela `4 fois` à l'aide d'une
    boucle . La fonction `forward`

    Arguments:

    :param longueur: désigne la mesure du côté du carré
    :type longueur: entier ou réel
    :param couleur: désigne le remplissage du carré
    :type couleur: int ou float


    Retour:

    Un carré de rayon `longueur`
    """

    fillcolor(couleur)
    begin_fill()
    for i in range(4):
        forward(longueur)
        left(90)
    end_fill()


def triangle(longueur, couleur):
    """Objectif:

    Dessine un triangle rectangle isocèle de longueur donné.

    Méthode:

    Le triangle est obtenu en traçant la base (qui est l'ypoténus) à
    l'aide de la valeur saisie en param. Les deux autres côtés du
    triangle ont été obtenus grâce à la méthode d Pythagore :
    `cote1 = cote2 = longueur / sqrt(2)`

    Arguments:

    :param longueur: désigne la mesure du côté du carré
    :type longueur: int ou float
    :param couleur: désigne le remplissage du triangle
    :type couleur: entier ou réel

    Retour:

    Un triangle de rayon `rayon`
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


def rectangle(longueur, largeur, couleur):
    """Objectif:

    Dessine un rectangle de dimensions données.

    Méthode:

    On trace la longueur et la largeur du rectangle en faisant une 
    rotation de 90° puis on répète la procédure 2 fois.

    Arguments:

    :param longueur, largeur: désigne les dimensions du rectangle
    :type longueur, largeur: entier ou réel
    :param couleur: désigne le remplissage du rectangle
    :type couleur: int ou float

    Retour:

    Un rectangle de dimension `longueur` et `largeur`
    """

    fillcolor(couleur)
    begin_fill()
    for i in range(2):
        forward(longueur)
        left(90)
        forward(largeur)
        left(90)
    end_fill()


def polygone(cote, nb_cote, couleur):
    """Objectif:

    Dessine un polygone de côté donné.

    Méthode:

    Le polygone a été obtenu à l'aide de `turtle.circle` avec le 
    param `steps` qui designe le nombre de côtés.

    Arguments:

    :param cote, nb_cote: désigne respectivement la longueur et le 
                          nombre de côté du polygone
    :type cote: entier ou réel
    :type nb_cote: entier
    :param couleur: désigne le remplissage du polygone
    :type couleur: int ou float

    Retour:

    Un polygone avec les dimensions `cote` et `nb_cote`
    """

    fillcolor(couleur)
    begin_fill()
    turtle.circle(cote, steps=nb_cote)
    end_fill()


def trapeze(longueur, petite_base, couleur):
    """Objectif:

    Dessine un trapèze de côté donné.

    Méthode:

    La grande base est obtenu à l'aide de la longeur qui désigne 
    l'hypoténus des triangles périphériques et de la petite base 
    avec la formule suivante : 
    `grande_base = 2 * longueur / sqrt(2) + petite_base`

    Arguments:

    :param longueur, petite_base: designent respectivement 
                                  l'hypoténus et la petite base
    :type longueur, petite_base: entier ou réel
    :param couleur: désigne le remplissage du trapèze
    :type couleur: int ou float

    Retour:

    Un trapeze
    """

    fillcolor(couleur)
    begin_fill()
    forward(longueur / sqrt(2))
    forward(petite_base)
    forward(longueur / sqrt(2))
    left(135)
    forward(longueur)
    left(45)
    forward(petite_base)
    left(45)
    forward(longueur)
    left(135)
    end_fill()


def losange(longueur, couleur):
    """Objectif:

    Dessine un losange de longueur donné.

    Méthode:

    Les côtées ont été tracé grâce à la méthode `forward` de `turlte`
    suivi des rotations à l'aide de sa méthode `left`.

    Arguments:

    :param longueur: designe la longueur des côtés du losange
    :type longueur: entier ou réel
    :param couleur: désigne le remplissage du losange
    :type couleur: chaîne de caractère

    Retour:

    Un losange
    """

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
    """Objectif:

    Dessine un ellipse de rayon donné.

    Méthode:

    La figure est obtenu avec la méthode `circle` de `turtle`

    Arguments:

    :param rayon: designe la longueur des côtés du losange
    :type rayon: entier ou réel
    :param couleur: désigne le remplissage de l'ellipse
    :type couleur: chaîne de caractère

    Retour:

    Un ellipse
    """

    fillcolor(couleur)
    begin_fill()
    left(45)
    for i in range(2):
        circle(rayon, 90)
        circle(rayon / 2, 90)
    end_fill()
