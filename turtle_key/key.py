import turtle

robot = turtle.Turtle()
robot.color = "black"

win = turtle.Screen()

def right():
    robot.right(90)

def left():
    robot.left(90)

def forward():
    if((robot.xcor()+50<=400 and robot.xcor()-50>=-400) and (robot.ycor()+50<=400 and robot.ycor()-50>=-400)):
        robot.forward(50)
    else:
        robot.goto(0,0)
def backward():
    if((robot.xcor()+50<=400 and robot.xcor()-50>=-400) and (robot.ycor()+50<=400 and robot.ycor()-50>=-400)):
        robot.backward(50)
    else:
        robot.goto(0,0)

win.title("My game")
win.bgcolor("green")
win.setup(width=800, height=800)

win.listen() 
win.onkey(forward, "Up")
win.onkey(backward, "Down")
win.onkey(right, "Right")
win.onkey(left, "Left")

win.mainloop()
