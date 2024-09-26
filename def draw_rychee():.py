from turtle import *

def draw_rychee():
    import turtle as t
    t.setup(800,800, 800, 800)
    t.penup()
    t.fd(-10)
    t.pendown()
    t.seth(-6)
    t.pensize(15)
    t.pencolor("red")
    for i in range(8):
        t.circle(40, 40)
        t.circle(-40, 80)
    t.circle(40, 180 / 2)
    t.fd(40)
    t.circle(16, 180)
    t.fd(40 * 2 / 3)
    t.circle(28, 150)
    t.fd(40 * 4 / 3)
    for i in range(6):
        fd(1)
        left(3)
    circle(80, 40)

    for i in range(20):
        fd(0.5)
        left(5)
    circle(80, 45)

    for i in range(10):
        fd(1)
        left(1)
    circle(80, 25)
    for i in range(6):
        fd(2)
        left(5)
    circle(80, 40)

    for i in range(20):
        fd(1)
        left(5)
    circle(80, 45)

    for i in range(10):
        fd(2)
        left(1)
    circle(80, 25)
    t.done()

from turtle import *

def draw_pig():
    import turtle as t
    t.setup(800, 800, 800, 800)
    t.penup()
    t.goto(0, -100)  # Start position
    t.pendown()
    t.pensize(5)
    t.pencolor("pink")

    # Draw the body
    t.begin_fill()
    t.circle(100)  # Main body
    t.end_fill()

    # Draw the head
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.begin_fill()
    t.circle(50)  # Head
    t.end_fill()

    # Draw the eyes
    for x in [-20, 20]:  # Positions for eyes
        t.penup()
        t.goto(x, 70)
        t.pendown()
        t.begin_fill()
        t.circle(10)  # Eyes
        t.end_fill()

    # Draw the nose
    t.penup()
    t.goto(0, 40)
    t.pendown()
    t.begin_fill()
    t.circle(15)  # Nose
    t.end_fill()

    # Draw nostrils
    for x in [-5, 5]:  # Positions for nostrils
        t.penup()
        t.goto(x, 40)
        t.pendown()
        t.begin_fill()
        t.circle(5)  # Nostrils
        t.end_fill()

    # Draw ears
    t.penup()
    t.goto(-40, 85)  # Left ear
    t.pendown()
    t.begin_fill()
    t.goto(-70, 120)
    t.goto(-40, 100)
    t.goto(-40, 85)
    t.end_fill()

    t.penup()
    t.goto(40, 85)  # Right ear
    t.pendown()
    t.begin_fill()
    t.goto(70, 120)
    t.goto(40, 100)
    t.goto(40, 85)
    t.end_fill()
    t.done()




print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Please select what you want to draw:\n"
              " (1 for rychee, 2 for pig)\n"
              "Your selection is: ")
    try:
        a = eval(a)
        if a == 1:
            draw_rychee()
        elif a == 2:
            draw_pig()
        else:
            print("Please input the value in [1]")
    except:
        print("Please input the value in [1]")
