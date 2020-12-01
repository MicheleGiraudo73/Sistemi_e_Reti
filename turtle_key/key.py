import turtle

robot = turtle.Turtle()
robot.color = "white"
width=800
height=400
lung=20

win = turtle.Screen()

def right():
    robot.right(90)

def left():
    robot.left(90)

def forward():
    if((robot.xcor()+lung<=width//2 and robot.xcor()-lung>=-width//2) and (robot.ycor()+lung<=height//2 and robot.ycor()-lung>=-height//2)):
        robot.forward(lung)
    else:
        robot.reset()
        robot.goto(0,0)
def backward():
    if((robot.xcor()+lung<=width//2 and robot.xcor()-lung>=-width//2) and (robot.ycor()+lung<=height//2 and robot.ycor()-lung>=-height//2)):
        robot.backward(lung)
    else:
        robot.reset()
        robot.goto(0,0)

win.title("My game")
win.bgcolor("green")
win.setup(width, height)

win.listen() 
win.onkey(forward, "Up")
win.onkey(backward, "Down")
win.onkey(right, "Right")
win.onkey(left, "Left")

win.mainloop()
