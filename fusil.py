import turtle


turtle.goto(-50, 0)
turtle.pensize(2)

# triangle
for i in range(3):
    turtle.forward(100)
    turtle.left(120)
pos1 = turtle.position()
# carré
turtle.penup()
turtle.goto(-25, 0)
turtle.pendown()
for i in range(4):
    turtle.forward(48)
    turtle.left(90)

def trapeze(a, b):
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(b)
    turtle.left(60)
    turtle.forward(b)
    turtle.left(60)
    turtle.forward(b)

# trapèze
turtle.penup()
turtle.setposition(-100.00, -87.00)
turtle.pendown()
trapeze(200, 100)
# rectangle
turtle.penup()
turtle.setposition(pos1)
turtle.left(30)
turtle.pendown()
turtle.forward(88)
turtle.penup()
turtle.setposition(50.00,0.00)
turtle.pendown()
turtle.forward(88)

# trapèze
turtle.penup()
turtle.setposition(-115.00, -114.00)
turtle.left(90)
turtle.pendown()
turtle.forward(230)
turtle.left(120)
turtle.forward(30)
turtle.left(60)
pos2 = turtle.position()
turtle.forward(200)
turtle.left(60)
pos3 = turtle.position()
turtle.forward(30)
# rectangle
turtle.penup()
turtle.goto(pos3)
turtle.left(30)
turtle.pendown()
turtle.forward(26)
pos4 = turtle.position()
turtle.penup()
turtle.goto(pos2)
turtle.pendown()
turtle.forward(26)
pos5 = turtle.position()

# rectangle
turtle.penup()
turtle.setposition(-115.00, -147.00)
turtle.left(90)
turtle.pendown()
turtle.forward(230)
turtle.left(90)
turtle.forward(33)
turtle.left(90)
turtle.forward(230)
turtle.left(90)
turtle.forward(33)
# semi-rectangle
turtle.penup()
turtle.goto(pos4)
turtle.pendown()
turtle.forward(33)
pos6 = turtle.position()
turtle.penup()
turtle.goto(pos5)
turtle.pendown()
turtle.forward(33)
pos7 = turtle.position()

# triangle quelconque
turtle.penup()
turtle.setposition(pos6)
turtle.right(8)
turtle.pendown()
turtle.forward(50)
turtle.right(162)
turtle.forward(50)

# triangle quelconque
turtle.penup()
turtle.setposition(pos7)
turtle.left(170)
turtle.left(8)
turtle.pendown()
turtle.forward(50)
turtle.left(162)
turtle.forward(50)

# rectangle
turtle.penup()
turtle.setposition(-20.00,-147.02)
turtle.left(190)
turtle.pendown()
for i in range(2):
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)

# cercles
turtle.penup()
turtle.setposition(-80.00,-170.02)
turtle.pendown()
turtle.circle(18)

turtle.penup()
turtle.setposition(45.00,-170.02)
turtle.pendown()
turtle.circle(18)

# rectangle
turtle.penup()
turtle.setposition(-50.00,-197.02)
turtle.pendown()
for i in range(2):
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

# carré
turtle.penup()
turtle.setposition(-15.00,-237.02)
turtle.pendown()
for i in range(4):
    turtle.forward(30)
    turtle.left(90)

# cercles
turtle.penup()
turtle.setposition(-30.00,-255.02)
turtle.left(90)
turtle.pendown()
turtle.circle(5)

turtle.penup()
turtle.setposition(30.00,-255.02)
turtle.pendown()
turtle.circle(5)

# trapeze
turtle.penup()
turtle.setposition(-75.00,-310.02)
turtle.pendown()
turtle.forward(144)
turtle.left(142)
turtle.forward(78)
turtle.left(40)
turtle.forward(30)
turtle.left(30)
turtle.forward(77)



turtle.done()