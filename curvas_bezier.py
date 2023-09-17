from turtle import *
import math
import random

origen_x = 0
origen_y = 0

def crear_tortuga():
    proyecto = Turtle(shape='turtle')
    proyecto.hideturtle()
    proyecto.speed(0)
    proyecto.left(45)
    proyecto.showturtle()
    return proyecto
    
window = Screen()
window.setup(800, 600)

mi_tortuga = crear_tortuga()
mi_tortuga.color(random.choice(['red', 'green', 'blue', 'purple', 'black']))
a = 100
b = 80
t = -89 
while (t < 270): 
    if t < 90 or t > 90:
        x = a * (math.cos(math.radians(t)))**-1 + origen_x
        y = b * math.tan(math.radians(t)) + origen_y
        mi_tortuga.goto(x, y)
    t += 1
window.exitonclick()
