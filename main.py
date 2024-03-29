# import colorgram
import turtle as t
import tkinter as tk
from tkinter import ttk
import random

cursor = t.Turtle()
t.colormode(255)
cursor.speed(0)

# rgb_colors = []
# colors = colorgram.extract("hirst-dots.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]

cursor.setheading(225)
cursor.penup()
cursor.hideturtle()
cursor.forward(300)
cursor.setheading(0)

num_dots = 100

for dot_count in range(1, num_dots +1):
    cursor.dot(20,random.choice(color_list))
    cursor.forward(50)

    if dot_count % 10 == 0:
        cursor.setheading(90)
        cursor.forward(50)
        cursor.setheading(180)
        cursor.forward(500)
        cursor.setheading(0)


screen = t.Screen()
screen.exitonclick()