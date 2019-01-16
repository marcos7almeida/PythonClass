# import random as rd
# import pylab as plb
# import turtle
# import time
#
# joe = turtle.Turtle()
#
# joe.penup()
# joe.goto(0, 0)
# joe.pendown()
#
# joe.pensize(4)

# joe.forward(100)
# joe.left(90)
# joe.forward(100)
# joe.left(90)
# joe.forward(100)
# joe.left(90)
# joe.forward(100)
# joe.left(90)
#
# joe.forward(100)
# joe.right(90)
# joe.forward(100)
# joe.right(90)
# joe.forward(100)
# joe.right(90)
# joe.forward(100)
# joe.right(90)
#
# joe.penup()
# joe.goto(150,50)
# joe.pendown()
#
# joe.forward(100)
# joe.left(90)
# joe.forward(100)
# joe.left(90)
# joe.forward(100)
# joe.left(90)
# joe.forward(100)
# joe.left(90)

# joe.forward(100)
# joe.right(90)
# joe.forward(100)
# joe.right(90)
# joe.forward(100)
# joe.right(90)
# joe.forward(100)
# joe.right(90)

# square
# for _ in range(4):
#     joe.forward(100)
#     joe.left(90)
#
# joe.clear()
# # string_1
# joe.pencolor('blue')
# for _ in range(3):
#     joe.forward(100)
#     joe.left(120)
# turtle.mainloop()
#
#
#
# time.sleep(10)
###############################
# import random as rd
# import pylab as plb
# import turtle
# import time
#
# def go(obj, x=0,y=0):
#         obj.penup()
#         obj.goto(x, y)
#         obj.pendown()
#
# joe = turtle.Turtle()
#
# go(joe, x=50, y=50)
#
# time.sleep(10)
##############################
# import random as rd
# import pylab as plb
# import turtle
# import time
#
#
# def go(obj, x=0,y=0):
#     obj.penup()
#     obj.goto(x, y)
#     obj.pendown()
#
# def square(obj, size):
#     for _ in range(4):
#         obj.forward(size)
#         obj.left(90)
#
# joe = turtle.Turtle()
#
# go(joe, x=50, y=50)
# square(joe,100)
#
# go(joe, x=100, y=100)
# square(joe,100)
#
#
# turtle.mainloop()
#########################
#import random as rd
#import pylab as plb
# import turtle
# import random as rd
#
# drunk = turtle.Turtle(shape='circle')
# step = 10
#
# for _ in range(1000):
#     if rd.random() < 0.5:
#         drunk.forward(step)
#     else:
#         drunk.backward(step)
# turtle.mainloop()
######################

import turtle
import random as rd
import pylab as plb

drunk = turtle.Turtle(shape='circle')
step = 10
p_step = 0.5
p_angle = 0.5

X_drunk = []

for _ in range(100):
    print(drunk.pos())

    X_drunk.append(drunk.pos()[0])

    if rd.random() < p_angle:
        drunk.left(90)
    else:
        drunk.left(-90)

    if rd.random() < p_step:
        drunk.forward(step)
    else:
        drunk.backward(step)
plb.plot(X_drunk, '-')
plb.title('Random Walk - Drunk')
plb.ylabel('X')
plb.xlabel('Time(step)')

plb.show()
plb.close()

plb.hist(X_drunk)
plb.show()
plb.close()

turtle.mainloop()
