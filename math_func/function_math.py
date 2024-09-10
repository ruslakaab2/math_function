import turtle
def func_math_ykxb(k,b):
    import turtle
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.setworldcoordinates(-10, -10, 10, 10)
    def area_drawing():
        screen.tracer(2)
        turtle.penup()
        turtle.goto(-10, 0)
        turtle.pendown()
        turtle.goto(10, 0)
        turtle.penup()
        turtle.goto(0, -10)
        turtle.pendown()
        turtle.goto(0, 10)

        turtle.up()

        for i in range(-10, 11):
            if i != 0:
                turtle.goto(i, 0)
                turtle.write(i, align="center")
                turtle.goto(0, i)
                turtle.write(i, align="center")
        screen.tracer(1)
        turtle.down()


    def plot_line(k, b):
        turtle.penup()
        turtle.goto(-10, k * (-10) + b)
        turtle.pendown()
        for x in range(-10, 11):
            y = k * x + b
            turtle.goto(x, y)

    area_drawing()
    plot_line(k, b)

    turtle.mainloop()


def draw_graph(k):
    import turtle


    screen = turtle.Screen()
    screen.tracer(2)
    t = turtle.Turtle()
    screen.setup(width=600, height=600)
    screen.setworldcoordinates(-10, -10, 10, 10)


    def area_drawing():
        t.speed(0)
        t.penup()
        t.goto(-10, 0)
        t.pendown()
        t.goto(10, 0)
        t.penup()
        t.goto(0, -10)
        t.pendown()
        t.goto(0, 10)
        t.penup()
        for i in range(-10, 11):
            if i != 0:
                t.goto(i, 0)
                t.write(i, align="center")
                t.goto(0, i)
                t.write(i, align="center")


    def plot_line(k):
        t.penup()
        t.goto(-10, k * (-10))
        t.pendown()
        for x in range(-10, 11, 1):
            if x != 0:
                y = k / x
                t.goto(x, y)

    area_drawing()
    screen.tracer(1)
    plot_line(k)
    turtle.mainloop()


import turtle


def draw_parabola():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.setworldcoordinates(-10, -10, 10, 1000)


    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()


    pen.goto(-10, 0)
    pen.pendown()
    pen.goto(10, 0)
    pen.penup()
    pen.goto(0, -10)
    pen.pendown()
    pen.goto(0, 1000)
    pen.penup()


    for i in range(-9, 10):
        if i != 0:
            pen.goto(i, -0.5)
            pen.write(str(i), align="center")
        if i != 0:
            pen.goto(-0.5, i)
            pen.write(str(i * 100), align="right")




    pen.penup()
    pen.goto(-10, 0)
    pen.pendown()

    for x in range(-100, 101):
        y = (x / 10) ** 3
        pen.goto(x / 10, y)


    pen.penup()
    pen.hideturtle()
    turtle.done()



def opred_func(func,k=0,b=0):
    if func=="k*x+b":
        func_math_ykxb(k,b)
    if func=="k/x":
        draw_graph(k)
    if func=="x^3":
        draw_parabola()

