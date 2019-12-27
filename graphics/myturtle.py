import turtle
import random

wn = turtle.Screen()
wn.title("My Turtle")
wn.colormode(255)

my_turtle = turtle.Turtle()

shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']

while True:
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    my_turtle.forward(150)
    my_turtle.right(65)
    my_turtle.forward(150)
    my_turtle.right(45)
    my_turtle.shape(shapes[random.randint(0, shapes.__len__()-1)])
    my_turtle.fillcolor(color)
    my_turtle.pencolor(color)

wn.mainloop()


