import turtle
import time
import random

delay = 0.1
score = 0
highest_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @Oskar_Wild_")
wn.bgcolor("#FCE883")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("purple")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0   High Score: 0", align="center", font=("Courier", 24, "normal"))


# Apple
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0, 100)

segments = []

# Functions
def go_up():
	if head.direction != "down":
		head.direction = "up"

def go_down():
	if head.direction != "up":
		head.direction = "down"

def go_right():
	if head.direction != "left":
		head.direction = "right"

def go_left():
	if head.direction != "right":
		head.direction = "left"

def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 20)
	elif head.direction == "down":
		y = head.ycor()
		head.sety(y - 20)
	elif head.direction == "right":
		x = head.xcor()
		head.setx(x + 20)
	elif head.direction == "left":
		x = head.xcor()
		head.setx(x - 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")

# Main game loop
while True:
	wn.update()
	# Check for a collision with food
	if head.distance(food) < 20:
		# Move the food to the random
		x = random.randint(-290, 290)
		y = random.randint(-290, 290)
		food.goto(x, y)
		score += 10
		if score > highest_score:
			highest_score = score
		pen.clear()
		pen.write("Score: {}   High Score: {}".format(score, highest_score), align="center", font=("Courier", 24, "normal"))
		

		# Add a segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("circle")
		new_segment.color("#BF40BF")
		new_segment.penup()
		segments.append(new_segment)

	# Move the end segments first in reverse order
	for index in range(len(segments)-1, 0, -1):
		x = segments[index - 1].xcor()
		y = segments[index - 1].ycor()
		segments[index].goto(x, y)

	# Move segment 0 to where the head is
	if segments != []:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)

	# Check the boarders
	if head.ycor() > 290 or head.ycor() < -290 or head.xcor() > 290 or head.xcor() < -290:
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "stop"
		score = 0
		pen.clear()
		pen.write("Score: 0   High Score: {}".format(highest_score), align="center", font=("Courier", 24, "normal"))


		# Hide the segments
		for segment in segments:
			segment.goto(1000, 1000)

		# Clear the segmets list
		segments = []

	move()

	# Check for head collision with the body segments
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0, 0)
			head.direction = "stop"
			for segment in segments:
				segment.goto(1000, 1000)
			segments = []
			score = 0
			pen.clear()
			pen.write("Score: 0   High Score: {}".format(highest_score), align="center", font=("Courier", 24, "normal"))

	time.sleep(delay)

wn.mainloop()

