import turtle 
import random


def tree(size, origsize):
    if size > 0:
        turtle.forward(size)
        r = random.randint(12, 30) if origsize < size else 60
        l = random.randint(12, 30) if origsize < size else 60
        turtle.pencolor("green")
        turtle.right(r)
        tree(size - random.randint(7, 10), origsize)
        turtle.left(r + l)
        tree(size - random.randint(7, 10), origsize)
        turtle.right(l)
        turtle.backward(size)
turtle.shape("turtle")
  



size=60 
origsize =55
turtle.tracer(7,0) 
turtle.mode('logo') 
turtle.pu() 
turtle.bk(size*2)
turtle.pd()
tree(size, origsize) 
turtle.exitonclick()
