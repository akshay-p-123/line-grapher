import turtle as trtl
import math

wn = trtl.Screen()
painter = trtl.Turtle()
wn.screensize(500)
wn.bgcolor("#b6b8ba")
painter.pensize(1.5)
running = True

#draw axes
painter.penup()
painter.goto(0, 250)
painter.setheading(270)
painter.pendown()
painter.forward(500)
painter.penup()
painter.goto(-400, 0)
painter.setheading(0)
painter.pendown()
painter.forward(800)


def draw_line(slope, y_int, turtle, color):
  turtle.color(color)
  turtle.hideturtle()
  turtle.penup()
  turtle.goto(0, y_int * 10)
  turtle.setheading(math.atan(slope) * 180/math.pi)
  turtle.pendown()
  turtle.forward(300)
  turtle.penup()
  turtle.goto(0, y_int * 10)
  turtle.pendown()
  turtle.forward(-300)
  if y_int > 0 and slope == 1:
    print("Equation: y = x + " + str(y_int))
  elif y_int > 0 and slope != 1:
    print("Equation: y = " + str(slope) + "x + " + str(y_int))
  if y_int == 0 and slope == 1:
    print("Equation: y = x")
  elif y_int == 0 and slope != 1:
    print("Equation: y = " + str(slope) + "x")
  if y_int < 0 and slope == 1:
    print("Equation: y = x " + str(y_int))
  elif y_int < 0 and slope != 1:
    print("Equation: y = " + str(slope) + "x " + str(y_int))
    
while running:
  slope = input("Enter the slope of your line.\n")
  y_intercept = input("Enter the y-intercept of your line.\n")
  color = input("Enter the color of your line.\n")
  draw_line(float(slope), float(y_intercept), painter, color)
  question = input("Draw another line? (y/n) ")
  if question.lower() != 'y':
    running = False
    
    
wn.mainloop()
