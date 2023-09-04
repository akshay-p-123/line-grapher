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
painter.goto(-600, 0)
painter.setheading(0)
painter.pendown()
painter.forward(1200)

#draw line
def draw_line(slope: float, y_int: float, turtle, color):
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
  
  output_string = "Equation: y = "

  if slope == 0 and y_int == 0:
    output_string += "0"
  if slope == 1:
    output_string += "x"
  elif slope == 0:
    pass
  else:
    output_string += (str(slope) + "x")

  if y_int > 0:
    output_string += (" + " + str(y_int))
  elif y_int < 0:
    output_string += (" - " + str(abs(y_int)))

  print(output_string)
  
  
while running:
  slope = input("Enter the slope of your line.\n")
  y_intercept = input("Enter the y-intercept of your line.\n")
  color = input("Enter the color of your line.\n")
  try:
    draw_line(float(slope), float(y_intercept), painter, color)
  except:
    try:
      draw_line(float(slope), float(y_intercept), painter, 'red')
    except:
      draw_line(0, 0, painter, 'red')
  question = input("Draw another line? (y/n) ")
  if question.lower() != 'y':
    running = False
    
    
wn.mainloop()
