"""
Dependencies: turtle
See: https://www.geeksforgeeks.org/draw-tree-using-turtle-module-in-python/
"""

import math
import time
import turtle


def _open_screen():
    turtle.color('deep pink')
    turtle.hideturtle()
    screen = turtle.Screen()
    screen.bgcolor('skyblue')


# Function to draw rectangle
def _draw_rectangle(tip, width, height, color):
    tip.fillcolor(color)
    tip.begin_fill()
    tip.forward(width)
    tip.left(90)
    tip.forward(height)
    tip.left(90)
    tip.forward(width)
    tip.left(90)
    tip.forward(height)
    tip.left(90)
    tip.end_fill()


# Function to draw triangle
def _draw_triangle(tip, length, color):
    tip.fillcolor(color)
    tip.begin_fill()
    tip.forward(length)
    tip.left(135)
    tip.forward(length / math.sqrt(2))
    tip.left(90)
    tip.forward(length / math.sqrt(2))
    tip.left(135)
    tip.end_fill()


def _draw_tree():
    # Creating turtle object
    tip = turtle.Turtle()
    tip.color('black')
    tip.shape('turtle')
    tip.speed(2)

    # Tree base
    tip.penup()
    tip.goto(100, -130)
    tip.pendown()
    _draw_rectangle(tip, 20, 40, 'brown')

    # Tree top
    tip.penup()
    tip.goto(65, -90)
    tip.pendown()
    _draw_triangle(tip, 90, 'lightgreen')
    tip.penup()
    tip.goto(70, -45)
    tip.pendown()
    _draw_triangle(tip, 80, 'lightgreen')
    tip.penup()
    tip.goto(75, -5)
    tip.pendown()
    _draw_triangle(tip, 70, 'lightgreen')


def _write_welcome_text():
    font = ('Courier', 20, 'italic')
    turtle.write('WELCOME TO WINGSPAN (TREE EDITION)!', font=font, align='center')


def welcome_message():
    _open_screen()
    _draw_tree()
    _write_welcome_text()
    time.sleep(2)
    turtle.bye()


if __name__ == '__main__':
    welcome_message()
