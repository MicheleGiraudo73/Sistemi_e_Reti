import turtle 
import random 

#larghezza e altezza della finestra di gioco
height = 400
width = 600

#snake
snake = turtle.Turtle()
snake.penup() #serve per non far muovere subito lo snake
snake.shape("square") #metto la forma quadrata alla testa dello snake
snake.speed(1)
snake.direction = "stop" #direzione dello snake

#cibo dello snake
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.pensize(5)
food.goto(random.randint(-(width/2),width/2),random.randint(-(height/2),height/2)) #randomizzo le coordinate

#funzioni per muoversi

def up():
    if snake.direction != "down":
        snake.direction = "up"

def down():
    if snake.direction != "up":
        snake.direction = "down"

def left():
    if snake.direction != "right":
        snake.direction = "left"

def right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

#setup della finestra
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width,height)

window.listen() 
window.onkeypress(up, "Up")
window.onkeypress(down, "Down")
window.onkeypress(right, "Right")
window.onkeypress(left, "Left")

while True:
	window.update()
	#questo if controlla che quando si tocca il bordo ri-inizi il game
	if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>190 or snake.ycor()<-190:
		snake.goto(0,0)
		snake.direction = "stop"
		food.clear()
	else:
		move()

	if snake.distance(food) < 15:
		food.goto(random.randint(-(width/2),width/2),random.randint(-(height/2),height/2))

window.mainloop()