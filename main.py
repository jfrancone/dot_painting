from turtle import Turtle, Screen
from colorpalette import palette, fall_palette, fall_palette_2, grand_canyon
import random

turns = [90, 180, 270, 360]
tina = Turtle()
tina.shape('turtle')
tina.speed("fastest")
position = tina.position()
print(position)
tina.pensize(0)
left_tina = True

screen = Screen()

screen.colormode(255)

def position_turtle():
    tina.penup()
    tina.goto(-225, -225)
    tina.pendown()

def dot_row(dot_number, c_palette):
    """
    (number of dots being drawn, list of colors) 
    Creates a row of dots across the screen. 
    Does not return a variable.
    """
    for _ in range((dot_number - 1)):
        rand_color = random.choice(c_palette)
        tina.dot(20, rand_color)
        tina.up()
        tina.forward(50)
        tina.down()
    tina.dot(20, (random.choice(c_palette)))

def hirst_dots(dot_number, c_palette, rows):
    """
    (# of dots per row, list of colors, # of rows) 
    Creates a hirst dot painting. 
    Does not return a variable.
    """
    left_tina = True
    for _ in range(rows):
        dot_row(dot_number, c_palette)
        if left_tina:
            tina.left(90)
            tina.up()
            tina.forward(50)
            tina.left(90)
            tina.down()
        else:
            tina.right(90)
            tina.up()
            tina.forward(50)
            tina.right(90)
            tina.down()
        left_tina = not left_tina
    

position_turtle()
#dot_row(10, palette)
hirst_dots(10, grand_canyon, 10)
new_position = tina.position()
print(new_position)

screen.exitonclick()

