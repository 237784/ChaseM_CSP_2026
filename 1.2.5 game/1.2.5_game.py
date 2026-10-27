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
wn.setup(width=1.0, height=1.0)
wn.addshape(red_balloon)
wn.addshape(blue_balloon)
wn.addshape(yellow_balloon)
wn.addshape(pink_balloon)
wn.bgpic("gamebackground.gif")
wn.tracer(False)

##Lists##
balloons = [red_balloon, blue_balloon, yellow_balloon, pink_balloon]
speed = [1, 2, 3, 4]

##Show them on the screen##
for i, balloon in enumerate(balloons):
    balloon_turtle = trtl.Turtle()
    balloon_turtle.shape(balloon)
    balloon_turtle.penup()
    balloon_turtle.goto(-100 + 50*i, -300)

wn.update()

trtl.mainloop()