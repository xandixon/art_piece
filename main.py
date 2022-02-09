import turtle as t
import random as r
import colorgram as cg

colors_f = []


def create_art(size_x, size_y, size, spacing):
    turtle = t.Turtle()
    t.colormode(255)
    turtle.penup()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(size)
    turtle.setheading(270)

    colors = cg.colorgram.extract('Resources/Samus_Returns.jpg', size_y)
    for color in colors:
        colors_f.append(color.rgb)

    start_x = size_x * -spacing / 2
    start_y = size_y * spacing / 2
    for i in range(0, size_y):
        turtle.setpos(start_x + spacing * i, start_y)
        dot_down(size_y, turtle, size, spacing)

    screen = t.Screen()
    screen.exitonclick()


def dot_down(num_dots, turtle, size, spacing):
    for i in range(num_dots):
        turtle.color(r.choice(colors_f))
        # turtle.color(colors_f[i])
        turtle.dot(size)
        turtle.forward(spacing)


def rand_color():
    return r.random(), r.random(), r.random()


create_art(10, 20, 10, 15)

