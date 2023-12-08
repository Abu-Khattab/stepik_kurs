from turtle import *


def star(side):
    shape('turtle')
    speed(20)
    for i in range(4):
        color("red")
        forward(side)
        left(90)


for _ in range(8):
    left(45)
    star(120)

setheading(90)

done()


''' next task '''

from turtle import *


def hexagon(side):
    speed(10)
    for i in range(6):
        color("red")
        forward(side)
        left(60)


side = 70
hexagon(side)

done()


''' next task '''

from turtle import *


def sota(side):
    speed(10)
    color('green')
    for i in range(6):
        forward(side)
        left(60)
    forward(side)
    right(60)


for _ in range(6):
    sota(100)

done()


''' next task '''


import turtle as t


def k(side):
    for i in range(1):
        t.forward(side)
        t.left(120)
        for j in range(2):
            t.forward(side)
            t.left(60)
            t.forward(side)
            t.left(120)


k(150)
t.done()


''' next task '''


import turtle

def rhombus():
    for i in range(1, 5):
        turtle.forward(100)
        turtle.right(120 - 60 * (i % 2))

for j in range(10):
    turtle.right(36)
    rhombus()

turtle.done()


''' next task '''

import turtle


def sneg(size):
    for i in ['red', 'yellow', 'green', 'orange', 'blue', 'purple'] * 2:
        turtle.color(i)
        turtle.forward(size)
        turtle.left(180)
        turtle.forward(size)
        turtle.left(30)


sneg(int(input()))


''' next task '''


import turtle

def cccp(size):
  for _ in range(5):
    turtle.forward(size)
    turtle.right(144)

turtle.pensize(3)
turtle.color('red')
cccp(int(input()))


''' next task '''

import turtle


for i in range(20, 200, 10):
    for _ in range(4):
      turtle.speed(20)
      turtle.left(90)
      turtle.forward(i)



''' next task '''

import turtle



for i in range(10,195,5):
  turtle.speed(20)
  turtle.left(90)
  turtle.forward(i)


