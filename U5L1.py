import turtle

t = turtle.Turtle()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

#Modify
import turtle

t = turtle.Turtle()

for i in range (4):
    t.forward(100)
    t.left(90)

#Part 2
import turtle

t = turtle.Turtle()

for i in range(3):
  t.forward(100)
  t.left(120)

#Modify
import turtle

t = turtle.Turtle()

for i in range(60):
  t.forward(100)
  t.left(63)
#Result in not a triangle

#Modify 2
import turtle

t = turtle.Turtle()

for i in range(80):
  t.forward(100)
  t.left(93)
#Part 3
import turtle

t = turtle.Turtle()
turtle.penup()
turtle.goto(100, 100)
turtle.dot(20, "red")
