import turtle


sequence = "-F+F+F-"
lenght = 10
angle = 90 
turtle.penup()  
turtle.goto(-400, +200)  
turtle.pendown() 
turtle.speed(1000)  

for symbol in sequence:
    if symbol == "F":
        turtle.forward(lenght)
    elif symbol == "-":
        turtle.left(angle)
    elif symbol == "+":
        turtle.right(angle)

turtle.done()
