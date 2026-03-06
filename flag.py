import turtle
t=turtle.Turtle()
t.begin_fill()
t.color("black")

for _ in range(2):
    t.forward(480)
    t.right(90)
    t.forward(90)
    t.right(90)
t.end_fill()

t.left(90)

t.penup()
t.backward(195)
t.pendown()
t.begin_fill()
t.right(90)

t.color("green")
for _ in range(2):
    t.forward(480)
    t.right(90)
    t.forward(90)
    t.right(90)
t.end_fill()
t.penup()
t.left(90)
t.forward(195)
t.right(90)
t.pendown()
t.begin_fill()

t.color("red")
t.right(45)
t.forward(200)
t.right(90)
t.forward(200)
t.right(135)
t.forward(285)
t.right(90)

t.end_fill()

turtle.done()

