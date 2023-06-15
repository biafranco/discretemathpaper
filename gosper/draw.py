import turtle


sequence = "+F++F-F--FF-F+"
lenght = 6
angle = 60
turtle.penup()  
turtle.goto(-400, +200)  
turtle.pendown() 
turtle.speed(300)  

for symbol in sequence:
    if symbol == "F":
        turtle.forward(lenght)
    elif symbol == "-":
        turtle.left(angle)
    elif symbol == "+":
        turtle.right(angle)

turtle.done()
