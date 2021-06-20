import turtle
import dessinMSDA


def maison():
    turtle.penup()
    turtle.goto(-100,-180)
    #turtle.left(90)
    turtle.pendown()
    dessinMSDA.carre(200,"orange")

    turtle.penup()
    turtle.goto(-125,20)
    #turtle.right(90)
    turtle.pendown()
    dessinMSDA.triangle(255,"brown")

    #porte
    turtle.penup()
    turtle.goto(-30,-165)
    turtle.pendown()
    turtle.left(90)
    dessinMSDA.rectangle(100,50,"gray")


    turtle.penup()
    turtle.goto(50,-45)
    turtle.pendown()
    for i in range(4):
        dessinMSDA.carre(25,"gray")
        turtle.right(90)

    turtle.penup()
    turtle.goto(70,70)
    turtle.pendown()
    dessinMSDA.rectangle(60,20,"brown")

    turtle.penup()
    turtle.goto(-100,-180)
    turtle.pendown()
    turtle.right(90)
    dessinMSDA.rectangle(200,15,"gray")

    turtle.penup()
    turtle.goto(-83,-179)
    turtle.pendown()
    #turtle.left(90)
    dessinMSDA.rectangle(56,12,"black")
    # fin
    turtle.penup()
    turtle.goto(0,-200)
    turtle.pendown()


if __name__ == "__main__":
    maison()
    turtle.done()
