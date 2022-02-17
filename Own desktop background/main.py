"""Create a desktop background(.png). The picture will be of different
 colored blocks. Its meant to look like  a pixeled window.
 First, ill get colorgram because there is there is a picture with colors that i like.
 second: use turtle to make me some cubes"""
import random
import colorgram
from turtle import Turtle, Screen

y = -400
x = 450
move_pixel_amount = 40
total_blokkies_per_ry = 30
total_rye = 1

color_option_two = ['#D06224', '#AE431E','#8A8635', '#E9C891', '#009DAE']
color_two_background = '#E9C891'
color_option_one = colorgram.extract("pixel_image.jpeg", 26)
color_one_background = "#94B49F"

list_of_colors = [color_option_one[i].rgb for i in range(0, 26)]

screen = Screen()
screen.setup(height=1000, width=1000)
screen.bgcolor(color_two_background)
screen.colormode(255)
screen.title("My own desktop background")

my_turtle = Turtle("square")
my_turtle.shapesize(stretch_len=2, stretch_wid=2)
my_turtle.penup()
my_turtle.goto(x=x, y=y)

for i in range(0, total_rye):
    y = -400 + (move_pixel_amount *(i+1))
    # total_blokkies_per_ry = total_blokkies_per_ry - (i)
    for i in range(0, total_blokkies_per_ry):
        my_turtle.color(random.choice(color_option_two))
        my_turtle.stamp()
        my_turtle.setheading(180)
        my_turtle.forward(move_pixel_amount)
    my_turtle.goto(x=x, y=y)

#save image as eps which i convert to jpeg in Gimp
user_input = screen.textinput("Save?", "Do you want to save the image? \n Yes to save. No to clear screen").lower()
if user_input == "yes":
    ts = my_turtle.getscreen()
    ts.getcanvas().postscript(file="image.eps")
else:
    screen.resetscreen()


screen.exitonclick()
