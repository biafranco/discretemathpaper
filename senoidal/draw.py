import turtle


sequence ="F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F-F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F++F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+FF-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F--F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F+F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F-F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F-F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F++F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+FF-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F--F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F+F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F++F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F-F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F++F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+FF-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F--F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F+F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+FF-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F-F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F++F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+FF-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F--F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F+F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F--F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F-F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F++F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+FF-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F--F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F+F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F+F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F-F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F++F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+FF-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F--F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F+F-F++FF--F+F-F-F++FF--F+F++F-F++FF--F+FF-F++FF--F+F--F-F++FF--F+F+F-F++FF--F+F"
lenght = 1
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
