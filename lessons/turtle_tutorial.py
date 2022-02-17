from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)
leo.penup()
leo.goto(50, 50)
leo.pendown()
leo.pencolor(200, 0, 0)
leo.fillcolor(0, 0, 255)
leo.speed(50)
leo.hideturtle()
leo.begin_fill()
i: int = 0 
while i < 4: 
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()
bob.pencolor(123, 212, 120)
bob.fillcolor(0, 0, 0)
bob.up()
bob.goto(50, 50)
bob.down()
bob.speed(100)
i: int = 0 
side_length: int = 300

while i < 4: 
    bob.forward(side_length)
    bob.left(120)
    i += 1
    
i: int = 0 

while i < 40: 
    side_length = side_length * 0.95
    bob.forward(side_length)
    bob.left(122)
    i += 1

done()