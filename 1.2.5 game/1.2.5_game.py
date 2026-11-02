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

##Game Functions##

##go up function##
def go_up(balloon_turtle, speed):
    balloon_turtle.sety(balloon_turtle.ycor() + speed*1.5)

    if balloon_turtle.ycor() >= 300:
        lose_game()
    else:
        wn.ontimer(lambda: go_up(balloon_turtle, speed), 50)
## Ballon Turtle     
balloon_turtle = trtl.Turtle()
balloon_turtle.penup()
balloon_turtle.speed(0)


##Score system##
font_setup = ("Coiny", 20, "normal")    
score = 0
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.speed(0)
score_writer.penup()
score_writer.goto(-300, 230)
score_writer.write("Score: " + str(score), font=font_setup, align="center")

##Pop balloon function##
    
##Losing function##
def lose_game():
    global score
    score_writer.clear()
    score_writer.goto(0, 0)
    score_writer.write("You Lose!", font=font_setup, align="center")
    score_writer.goto(0, -30)
    score_writer.write("Final Score: " + str(score), font=font_setup, align="center")
    lost = True
    wn.update()


##Balloon clicked##
def balloon_click(x, y): ##remove the current balloon from the screen and make a new one begin to move and update the score
    global clicked
    global balloons
    clicked = True
    reset_balloon()
    update_score()
    


##Update the score##
def update_score():
    global score
    global speed
    score += current_speed
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

    print("Balloon:", balloons[current_index])
    print("Speed:", current_speed)

lost = False
##Show them on the screen##
while True:
    reset_balloon()
    while lost == False:
        balloon_turtle.onclick(balloon_click)
        while balloon_turtle.ycor() < 300: 
            go_up(balloon_turtle, current_speed) 
            wn.update()  

        clicked = False
          
wn.listen()
wn.mainloop()