import turtle
import dessinMSDA


def maison():
    turtle.penup()
    turtle.goto(-100,-180)
    turtle.left(90)
    turtle.pendown()
    dessinMSDA.carre(200)

    turtle.penup()
    turtle.goto(-125,20)
    turtle.right(90)
    turtle.pendown()
    dessinMSDA.triangle(255)

    turtle.penup()
    turtle.goto(-30,-165)
    turtle.pendown()
    turtle.left(90)
    dessinMSDA.rectangle(100,50)


    turtle.penup()
    turtle.goto(50,-45)
    turtle.pendown()
    for i in range(4):
        dessinMSDA.carre(25)
        turtle.right(90)

    turtle.penup()
    turtle.goto(70,120)
    turtle.pendown()
    dessinMSDA.rectangle(60,20)

    turtle.penup()
    turtle.goto(-100,-180)
    turtle.pendown()
    turtle.right(90)
    dessinMSDA.rectangle(200,15)
turtle.done()
