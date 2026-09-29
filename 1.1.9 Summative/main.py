import turtle
import random
screen = turtle.Screen()
screen.bgcolor("beige")
screen.setup(width=800, height=800)
screen.tracer(0)
##Make the box that the turtles will move in##
display_width = 300 #half of the width of the display
display_height = 300 # half of the height of the display
display = turtle.Turtle()
display.hideturtle()
display.penup()
display.speed(0)
display.pensize(3)
display.goto(-display_width, -display_height)
display.pendown()
display.fillcolor("white")
display.begin_fill()
display.goto(display_width, -display_height)
display.goto(display_width, display_height)
display.goto(-display_width, display_height)
display.goto(-display_width, -display_height)
display.end_fill()
screen.update()
###############################################

##Ask the user how many turtles they want to create##
num_balls = screen.numinput("Circles", "How many Circles do you want?", minval=1, maxval=10, default=5)
#####################################################

##Put the selected number of turtles in a list##
balls = []
for i in range(int(num_balls)):
  ball = turtle.Turtle()
  ball.shape("circle")
  ball.color(random.random(), random.random(), random.random()) #random color
  ball.pencolor("black")
  ball.penup()
  ball.speed(3)
  x = random.randint(-270, 270) #Makes the start pos random in the box
  y = random.randint(-270, 270) #Makes the start pos random in the box
  ball.goto(x, y)

  ##Making the turtles not overlap##
  while True: 
    overlap = False
    for other_ball in balls:
      if ball.distance(other_ball) < 40: #Checks if the distance between the two turtles is less than 40 pixels
        overlap = True
        break
    if not overlap:
      break
    x = random.randint(-270, 270)
    y = random.randint(-270, 270)
    ball.goto(x, y)
    ###############################

  balls.append(ball)
  screen.update()
##################################################

##Making the collision counter##
collision_count = 0
collision_counter = turtle.Turtle()
collision_counter.hideturtle()
collision_counter.penup()
collision_counter.speed(0)
collision_counter.goto(0, display_height + 20)
collision_counter.write(f"Collisions: {collision_count}", align="center", font=("Arial", 16, "normal"))
################################

##Start the motion##


screen.mainloop()