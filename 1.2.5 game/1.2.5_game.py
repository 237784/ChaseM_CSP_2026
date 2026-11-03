#game - Rising Balloons
import turtle as trtl
import random as rand
import math as math

#import images
red_balloon = "_redballoon.gif"
blue_balloon = "_blueballoon.gif"
yellow_balloon = "_yellowballoon.gif"
pink_balloon = "_pinkballoon.gif"

##setting up the screen##
wn = trtl.Screen()
wn.title("Pop the ballons")
wn.setup(width=740, height=555)
wn.cv._rootwindow.resizable(False, False)
wn.addshape(red_balloon)
wn.addshape(blue_balloon)
wn.addshape(yellow_balloon)
wn.addshape(pink_balloon)
wn.bgpic("gamebackground.gif")
wn.tracer(1)
##Lists##
balloons = [red_balloon, blue_balloon, yellow_balloon, pink_balloon]
speed = [1, 2, 3, 4]

clicked = False

##Game Functions#

## Ballon Turtle     
balloon_turtle = trtl.Turtle()
balloon_turtle.penup()
balloon_turtle.speed(0)


##Score system##
font_setup = ("Coiny", 20, "normal")  
font_setup_s = ("Coiny", 12, "normal")  
score = 0
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.speed(0)
score_writer.penup()
score_writer.goto(-300, 230)
score_writer.write("Score: " + str(score), font=font_setup, align="center")

##go up function##
def go_up(balloon_turtle, speed):
    balloon_turtle.sety(balloon_turtle.ycor() + (speed*1.5)*(1.01**(score)))

'''
   if balloon_turtle.ycor() >= 300:
        lose_game()
    else:
        wn.ontimer(lambda: go_up(balloon_turtle, speed), 50)'''
    
##Losing function##
def lose_game():
    global lost
    global score
    score_writer.clear()
    score_writer.goto(0, 0)
    score_writer.write("You Lose!", font=font_setup, align="center")
    score_writer.goto(0, -30)
    score_writer.write("Final Score: " + str(score), font=font_setup, align="center")
    score_writer.goto(0, -60)
    score_writer.write("Press 'Space' to play again or 'q' to quit", font=font_setup, align="center")
    lost = True
    wn.update()

##Reset game function##
def reset_game():
    global lost
    global score
    global clicked
    if lost == True:
        score = 0
        score_writer.clear()
        score_writer.goto(-300, 230)
        score_writer.write("Score: " + str(score), font=font_setup, align="center")
        lost = False
        clicked = False
        reset_balloon()
        
    

##Balloon clicked##
def balloon_click(x, y): ##remove the current balloon from the screen and make a new one begin to move and update the score
    global clicked
    global balloons
    clicked = True
    update_score()
    reset_balloon()
    

##Update the score##
def update_score():
    global score
    global current_index
    score += speed[current_index]
    #print("added this many",speed[current_index])
    score_writer.clear()
    score_writer.write("Score: " + str(score), font=font_setup, align="center")
    wn.update()

current_speed = 0
current_index = 0

##Set the ballon off of screen
def reset_balloon():
    global current_speed
    global current_index

    current_index = rand.randint(0,(len(balloons)-1))
    current_speed = speed[current_index]

    balloon_turtle.hideturtle()
    balloon_turtle.shape(balloons[current_index])
    balloon_turtle.speed(0)
    balloon_turtle.goto(rand.randint(-300, 300), -300)
    balloon_turtle.showturtle()

   # print("Balloon:", balloons[current_index])
   # print("Speed:", current_speed)
    print("total multiplier:", 1.01**(score))

wn.listen()
wn.onkeypress(reset_game, "space")
wn.onkeypress(wn.bye, "q")

lost = False
##Show them on the screen##
while True:
    reset_balloon()
    balloon_turtle.onclick(balloon_click)
    while lost == False:
        balloon_turtle.onclick(balloon_click)
        #while balloon_turtle.ycor() < 300: 
        go_up(balloon_turtle, current_speed) 
        wn.update()  

        if clicked == True:
            clicked = False

        if balloon_turtle.ycor() >= 300:
            lose_game()

    if lost == True:
        wn.update()
