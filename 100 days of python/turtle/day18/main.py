from turtle import Turtle, Screen
from random import randint 

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.speed("fastest")


def draw_form(edges: int):
    for _ in range(edges):
        timmy_the_turtle.forward(40)
        timmy_the_turtle.right(360/edges)

def create_random_color():
    r = randint(0,100)/100
    g = randint(0,100)/100
    b = randint(0,100)/100
    return (r,g,b)

def draw_lotsa_shapes(amount: int):
    for i in range(3,amount):
        draw_form(i)
        color = create_random_color()
        timmy_the_turtle.pencolor(color)

def make_random_walk(steps:int,step_length:int=40):
    for _ in range(steps):
        timmy_the_turtle.pensize(10)
        timmy_the_turtle.forward(step_length)
        timmy_the_turtle.right(90*randint(0,3))
        timmy_the_turtle.pencolor(create_random_color())

def draw_spirograph(rad:int,density:int):
    for _ in range(density):
        timmy_the_turtle.circle(rad)
        timmy_the_turtle.right(360/density)
        timmy_the_turtle.pencolor(create_random_color())

def draw_dot_matrix(size:int, dots_per_line:int):
    timmy_the_turtle.hideturtle()
    step_size = size/dots_per_line
    dot_size = size/1.5/dots_per_line
    timmy_the_turtle.penup()
    pos = timmy_the_turtle.pos()
    timmy_the_turtle.goto(pos[0]-size/2,pos[1]-size/2)
    for _ in range(dots_per_line):
        for _ in range(dots_per_line):
            timmy_the_turtle.pencolor(create_random_color())
            timmy_the_turtle.dot(dot_size)
            timmy_the_turtle.forward(step_size)
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(step_size)
        timmy_the_turtle.setheading(180)
        timmy_the_turtle.forward(size)
        timmy_the_turtle.setheading(0)


            

# draw_lotsa_shapes(5)
# make_random_walk(100)
# draw_spirograph(200,300)
draw_dot_matrix(400,10 )

screen = Screen()
screen.exitonclick()