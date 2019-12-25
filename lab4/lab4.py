import turtle
import random
def mul(a,b):
    i = 1
    a2 = a
    b2 = b
    if (a < b):
        while (i < b):
            a += a2
            i += 1
        return a
    else:
        while (i < a):
            b += b2
            i += 1
        return b
       
 
def expo(a,b):
    new = 1
    for num in range(b):
        new = mul(a,new)
    return new
        
def div27(num):
    a = True
    for i in range(2,8):
        if num % i == 0:
            return True
        else:
            a = False
    return a

def turtlefunction():
    sqrt3 = 3**0.5

    leo = turtle.Turtle()
    leo.color("blue")
    leo.shape("arrow")
    mikey = turtle.Turtle()
    mikey.color("orange")
    mikey.shape("circle")
    don = turtle.Turtle()
    don.color("purple")
    don.shape("square")
    raph = turtle.Turtle()
    raph.color("red")
    raph.shape("turtle")

    leo.forward(50*sqrt3)
    mikey.setpos(-50*sqrt3,0)
    don.circle(50)
    leo.left(120)
    leo.forward(100*sqrt3)
    mikey.setpos(0,150)
    raph.left(90)
    raph.forward(150)

def turtlerace():
    racer1 = turtle.Turtle()
    racer2 = turtle.Turtle()
    racer3 = turtle.Turtle()
    turtle.setworldcoordinates(0,0,100,100)
    racer1.shape("turtle")
    racer2.shape("turtle")
    racer3.shape("turtle")
    racer1.color("red")
    racer2.color("blue")
    racer3.color("green")
    racer1.setheading(0)
    racer2.setheading(0)
    racer3.setheading(0)
    racer1.setx(0)
    racer2.setx(0)
    racer3.setx(0)
    racer1.sety(40)
    racer2.sety(50)
    racer3.sety(60)
    while(racer1.xcor() < 100 and racer2.xcor() < 100 and racer3.xcor() < 100):
        ran1 = random.randint(1,15)
        ran2 = random.randint(1,15)
        ran3 = random.randint(1,15)
        racer1.forward(ran1)
        racer2.forward(ran2)
        racer3.forward(ran3)
    if racer1.xcor() >= 100:
        print('red wins')
    elif racer2.xcor() >= 100:
        print('blue wins')
    elif racer3.xcor() >= 100:
        print('green wins')
                    
def checkerboard():
    turtle.setworldcoordinates(0,0,640,640)
    turtle.speed(0)
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

    turtle.penup()
    turtle.setpos(80,80)
    turtle.pendown()
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

    turtle.penup()
    turtle.setpos(0,160)
    turtle.pendown()
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

    turtle.penup()
    turtle.setpos(80,240)
    turtle.pendown()
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

    turtle.penup()
    turtle.setpos(0,320)
    turtle.pendown()
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

    turtle.penup()
    turtle.setpos(80,400)
    turtle.pendown()
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

    turtle.penup()
    turtle.setpos(0,480)
    turtle.pendown()
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

    turtle.penup()
    turtle.setpos(80,560)
    turtle.pendown()
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

    turtle.penup()
    turtle.setpos(0,640)
    turtle.pendown()
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

#_____________________________________________

    turtle.penup()
    turtle.setpos(80,0)
    turtle.pendown()
    turtle.color("red")
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

    turtle.penup()
    turtle.setpos(0,80)
    turtle.pendown()
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

    turtle.penup()
    turtle.setpos(80,160)
    turtle.pendown()
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

    turtle.penup()
    turtle.setpos(0,240)
    turtle.pendown()
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

    turtle.penup()
    turtle.setpos(80,320)
    turtle.pendown()
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

    turtle.penup()
    turtle.setpos(0,400)
    turtle.pendown()
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

    turtle.penup()
    turtle.setpos(80,480)
    turtle.pendown()
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

    turtle.penup()
    turtle.setpos(0,560)
    turtle.pendown()
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

    turtle.penup()
    turtle.setpos(80,640)
    turtle.pendown()
    for i in range(4):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(80)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(160)

