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
    balloon_turtle.sety(balloon_turtle.ycor() + speed*2)
    if balloon_turtle.ycor() < 300:
        wn.ontimer(lambda: go_up(balloon_turtle, speed), 50)
     


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
    wn.update()

##Balloon clicked##
def balloon_click(x, y): ##remove the current balloon from the screen and make a new one begin to move and update the score
    global clicked
    clicked = True
    balloon_turtle.hideturtle()

    balloon_turtle.goto(rand.randint(-300, 300), -300)
    


    balloon_turtle.showturtle()
    update_score()
    



##Update the score##
def update_score():
    global score
    global speed
    score += speed[i]
    score_writer.clear()
    score_writer.write("Score: " + str(score), font=font_setup, align="center")
    wn.update()

balloon_turtle = trtl.Turtle()

##Show them on the screen##
while True:
    #rand.shuffle(balloons)
    for i, balloon in enumerate(balloons):
        balloon_turtle.hideturtle() 
        balloon_turtle.shape(balloon)
        balloon_turtle.speed(0)
        balloon_turtle.penup()
        balloon_turtle.goto(rand.randint(-300, 300), -300)
        balloon_turtle.showturtle() 
        balloon_turtle.onclick(balloon_click)
        while balloon_turtle.ycor() < 300: 
            go_up(balloon_turtle, speed[i]) 
            wn.update()  
            print(clicked)
            if balloon_turtle.ycor() >= 300 and clicked is False:
                lose_game()
                break
        clicked = False
    
        
wn.listen()
wn.mainloop()