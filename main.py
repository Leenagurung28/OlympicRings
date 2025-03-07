import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('tan')

t = turtle.Turtle()

t.penup()
t.goto(0,15)
t.pendown()
#circle - radius
t.pendown()
t.pencolor('black')

t.circle(35)


#to move turtle to new place
t.penup()
t.goto(0,0)
t.pendown()

t.penup()
t.goto(80,15)
t.pendown()
#circle - radius
t.pendown()
t.pencolor('red')
t.circle(35)
#to move turtle to new place
t.penup()
t.goto(0,0)
t.pendown()
t.penup()
t.goto(-80,15)
t.pendown()
#circle - radius
t.pendown()
t.pencolor('blue')
t.circle(35)
#to move turtle to new place
t.penup()
t.goto(0,0)
t.pendown()
t.penup()
t.goto(-40,-10)
t.pendown()
#circle - radius
t.pendown()
t.pencolor('yellow')
t.circle(35)


#to move turtle to new place
t.penup()
t.goto(0,0)
t.pendown()
t.penup()
t.goto(40,-10)
t.pendown()
#circle - radius
t.pendown()
t.pencolor('green')
t.circle(35)

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor('purple')
t.write("Winter Olympics",font=("Cambria",30,"bold italic"),align="center")

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor('purple')
t.write("2026",font=("Cambria",30,"bold italic"),align="center")

#This is the last line of code
turtle.done()
