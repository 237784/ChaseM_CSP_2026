#game - Rising Balloons
import turtle as trtl
import random as rand

#import images
red_balloon = "_redballoon.gif"
blue_balloon = "_blueballoon.gif"
yellow_balloon = "_yellowballoon.gif"
pink_balloon = "_pinkballoon.gif"

##setting up the screen##
wn = trtl.Screen()
wn.setup(width=740, height=555)
wn.cv._rootwindow.resizable(False, False)
wn.addshape(red_balloon)
wn.addshape(blue_balloon)
wn.addshape(yellow_balloon)
wn.addshape(pink_balloon)
wn.bgpic("gamebackground.gif")
wn.tracer(1.1)
##Lists##
balloons = [red_balloon, blue_balloon, yellow_balloon, pink_balloon]
speed = [1, 2, 3, 4]


##go up function##
def go_up(balloon_turtle, speed):
    """Moves the balloon turtle up the screen at the specified speed."""
    balloon_turtle.sety(balloon_turtle.ycor() + speed*2)
    if balloon_turtle.ycor() < 300:  # Check if the balloon is still within the screen bounds
        wn.ontimer(lambda: go_up(balloon_turtle, speed), 50)  # Continue moving up after a short delay
##Show them on the screen##
for i, balloon in enumerate(balloons):
    balloon_turtle = trtl.Turtle()
    balloon_turtle.hideturtle() 
    balloon_turtle.shape(balloon)
    #balloon_turtle.speed(0)
    balloon_turtle.penup()
    balloon_turtle.goto(rand.randint(-300, 300), -300)
    balloon_turtle.showturtle()  # Show the turtle after setting its shape
    while balloon_turtle.ycor() < 300:  # Keep moving the balloon up until it reaches the top of the screen
        go_up(balloon_turtle, speed[i])  # Start moving the balloon up
        wn.update()  # Update the screen to reflect the changes


wn.mainloop()