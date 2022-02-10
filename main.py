import turtle as t
import random as r

colors_f = []


def create_art(size_x, size_y, size, spacing):
    turtle = t.Turtle()
    # t.colormode(255)
    turtle.penup()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(size)
    turtle.setheading(270)

    start_x = size_x/2 * -spacing
    start_y = size_y/2 * spacing
    for i in range(0, size_x):
        turtle.setpos(start_x + spacing * i, start_y)
        dot_down(size_y, turtle, size, spacing)

    screen = t.Screen()
    screen.exitonclick()


def dot_down(num_dots, turtle, size, spacing):
    for i in range(num_dots):
        turtle.color(rand_color())
        # turtle.color(colors_f[i])
        turtle.dot(size)
        turtle.forward(spacing)


def rand_color():
    return r.random(), r.random(), r.random()


input_x = int(input('X Dimension? (Max 25)\n'))
input_y = int(input('Y Dimension (Max 25?\n'))
create_art(input_x, input_y, 10, 15)


