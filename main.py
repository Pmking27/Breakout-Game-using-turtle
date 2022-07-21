import turtle
import tkinter
from cube import *
import time
import winsound

score_no = 0
FONT = ("Courier", 24, "normal")
winsound.PlaySound(
    "E:\my #100dayscodewithpython\Day 86 - Breakeout Game using Turtle [Game]\music\slow-trap.wav", winsound.SND_ASYNC | winsound.SND_LOOP | winsound.SND_FILENAME)

screen = turtle.Screen()
screen.setup(600, 670)
screen.title("Breakout Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

img = tkinter.Image(
    "photo", file="E:\my #100dayscodewithpython\Day 86 - Breakeout Game using Turtle [Game]\logo.png")
turtle._Screen._root.iconphoto(True, img)

paddle = turtle.Turtle(shape="square")
paddle.hideturtle()
paddle.penup()
paddle.speed(0)
paddle.setposition(0, -290)
paddle.color('white')
paddle.shapesize(1, 5)
paddle.showturtle()

borderline = turtle.Turtle()
borderline.penup()
borderline.hideturtle()
borderline.color("white")
borderline.goto(-300, 300)
borderline.pendown()
borderline.forward(600)

score = turtle.Turtle()
score.penup()
score.hideturtle()
score.color("white")
score.goto(-300, 300)
score.pendown()
score.forward(600)
score.goto(-300, 300)
screen.cv._rootwindow.resizable(False, False)

ball = turtle.Turtle()
ball.color('red')
ball.shape('circle')
ball.up()
ball.dx = 3
ball.dy = 4


def left_paddle():
    if paddle.xcor() > -210:
        paddle.goto(paddle.xcor()-40, paddle.ycor())


def right_paddle():
    if paddle.xcor() < 210:
        paddle.goto(paddle.xcor()+40, paddle.ycor())


screen.onkey(right_paddle, 'Right')
screen.onkey(left_paddle, 'Left')

x_pos = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]
y_pos = [250, 200, 150, 100]

cube_list = []

for i in x_pos:
    for j in y_pos:
        cube = Cube(i, j, '3', 'white', ball)
        cube_list.append(cube)
        cube.draw()

game_continue = True
while game_continue:
    score.clear()
    score.write(f"Score:{score_no}", align="left", font=FONT)
    screen.update()
    for i in cube_list:
        # Only render the cube if falling
        if i.fall == True:
            i.t.clear()
            i.t.color('red')
            i.draw()
        if i.xpos-25 <= ball.xcor() <= i.xpos+25:
            if i.ypos-20 <= ball.ycor() <= i.ypos+25 and i.fall == False:
                score_no += 1
                i.counter = 0.01
                i.fall = True
                ball.dy *= -1

        if i.fall == True:
            i.ypos -= 3
            i.counter += 0.05
            if i.ypos < -350:
                cube_list.remove(i)

    ball.goto(ball.xcor()+ball.dx, ball.ycor()+ball.dy)

    if ((ball.xcor() <= -280 and ball.dx < 0) or (ball.xcor() >= 280 and ball.dx > 0)):
        ball.dx *= -1
    if ball.ycor() > 280 and ball.dy > 0:
        ball.dy *= -1

    if (ball.xcor()-10 <= paddle.xcor()+50 and ball.xcor()+10 >= paddle.xcor()-50):
        if ball.ycor() <= paddle.ycor()+15 and ball.dy < 0:
            ball.dy *= -1

    if ball.ycor() < -330:
        ball.hideturtle()
        ball.goto(0, 0)
        ball.write("Game Over.", align="center", font=FONT)
        winsound.PlaySound(
            "E:\my #100dayscodewithpython\Day 86 - Breakeout Game using Turtle [Game]\music\mixkit-sad-game-over.wav", winsound.SND_ASYNC)
        time.sleep(3)
        game_continue = False

    if len(cube_list) == 0:
        for i in x_pos:
            for j in y_pos:
                cube = Cube(i, j, '3', 'white', ball)
                cube_list.append(cube)
                cube.draw()
