from turtle import Turtle, Screen
import turtle as t
import random

# use rgb_generate file to generate color list:
color_list = [(189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 212, 214),
               (64, 43, 43), (171, 183, 170), (136, 149, 69), (127, 160, 172),(101, 79, 89), (83, 133, 108),
               (108, 39, 44), (39, 61, 47), (45, 40, 41), (174, 150, 152), (36, 71, 88)]

t.colormode(255)
tim = Turtle()
tim.speed(40)
tim.hideturtle()

tim.setheading(225)
tim.penup()
tim.forward(300)
# tim.left(135) or
tim.setheading(0)

i = 0
while i<10:
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)

    tim.left(90)
    tim.penup()
    tim.forward(50)
    tim.left(90)
    tim.forward(50*10)
    tim.right(180)
    i += 1

screen = Screen()
screen.exitonclick()
