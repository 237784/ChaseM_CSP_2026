#game - Rising Balloons
import turtle as trtl
import random as rand
import math as math
import json
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
#########################

##Lists##
balloons = [red_balloon, blue_balloon, yellow_balloon, pink_balloon]
speed = [1, 2, 3, 4]
leaderboard = []
########


##Clicked variable for later##
clicked = False
##############################

##Game Functions#

##Open leaderboard##
def load_leaderboard():
    global leaderboard
    with open("leaderboard.json", "r") as file:
        leaderboard = json.load(file)
#########################

##Saving leaderboard##
def save_leaderboard():
    with open("leaderboard.json", "w") as file:
        json.dump(leaderboard, file)
#######################

##Adding score to leaderboard##
def add_score():
    global leaderboard

    name = wn.textinput("Leaderboard", "Enter your name:")
    
    if name == None or name.strip() == "":
        name = "Anonymous"

    name = name.strip()
    
    ##Check if name exists##
    existing_player = None

    for entry in leaderboard:
        if entry[0].lower() == name.lower():
            existing_player = entry
            break

    if existing_player != None:
        if score > existing_player[1]:
            existing_player[1] = score
    else:
        leaderboard.append([name, score])

    leaderboard.sort(key=lambda x: x[1], reverse=True)
    leaderboard = leaderboard[:5]
    ###########################
    save_leaderboard()
########################

##Ballon Turtle##
balloon_turtle = trtl.Turtle()
balloon_turtle.penup()
balloon_turtle.speed(0)
#################

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
##################

##go up function##
def go_up(balloon_turtle, speed):
    catch_up = abs(speed - 4) * (score * .01)
    balloon_turtle.sety(balloon_turtle.ycor() + (speed * 1.5 + catch_up) * (1.01 ** (score)))
##################

##Losing function##
def lose_game():
    global lost
    global score

    lost = True
    add_score()

    score_writer.clear()
    score_writer.goto(0, 0)
    score_writer.write("You Lose!", font=font_setup, align="center")
    score_writer.goto(0, -30)
    score_writer.write("Final Score: " + str(score), font=font_setup, align="center")
    score_writer.goto(0, -60)
    score_writer.write("Press 'Space' to play again or 'q' to quit", font=font_setup_s, align="center")

    show_leaderboard()
    wn.update()
####################

##Reset game function##
def reset_game():
    global lost
    global score
    global clicked
    if lost == True:
        score = 0
        score_writer.clear()
        leaderboard_writer.clear()
        score_writer.goto(-300, 230)
        score_writer.write("Score: " + str(score), font=font_setup, align="center")
        lost = False
        clicked = False
        reset_balloon()
########################    
    

##Balloon clicked##
def balloon_click(x, y):
    global clicked
    global balloons
    clicked = True
    update_score()
    reset_balloon()
####################

##Update the score##
def update_score():
    global score
    global current_index
    score += speed[current_index]
    #print("added this many",speed[current_index])
    score_writer.clear()
    score_writer.write("Score: " + str(score), font=font_setup, align="center")
    wn.update()
###################

##Makes stuff easier##
current_speed = 0
current_index = 0
#####################

##Put balloon back to bottom##
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
################################


##Leaderboard Turtle and showing it##
leaderboard_writer = trtl.Turtle()
leaderboard_writer.hideturtle()
leaderboard_writer.penup()
leaderboard_writer.speed(0)

def show_leaderboard():
    leaderboard_writer.clear()
    leaderboard_writer.goto(0, 200)

    leaderboard_writer.write("Leaderboard", font=font_setup, align="center")

    for i, entry in enumerate(leaderboard):
        leaderboard_writer.goto(0, 170 - (i * 30))
        leaderboard_writer.write(f"{entry[0]}: {entry[1]}", font=font_setup_s, align="center")
################################

##Game functions that are like in the game ya know##
load_leaderboard()
wn.listen()
wn.onkeypress(reset_game, "space")
wn.onkeypress(wn.bye, "q")
####################################################
lost = False

##Main loop##
while True:
    reset_balloon()
    balloon_turtle.onclick(balloon_click)
    while lost == False:
        balloon_turtle.onclick(balloon_click)
        #while balloon_turtle.ycor() < 300: 
        go_up(balloon_turtle, current_speed) 
        wn.update()
        wn.listen()  

        if clicked == True:
            clicked = False

        if balloon_turtle.ycor() >= 300:
            lose_game()

    if lost == True:
        wn.listen()
        wn.update()
