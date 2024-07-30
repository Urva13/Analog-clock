import turtle
import datetime

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Analog Clock")
screen.tracer(1)

# Create the clock face
clock_face = turtle.Turtle()
clock_face.hideturtle()
clock_face.penup()
clock_face.goto(0, -250)
clock_face.pendown()
clock_face.circle(250)

# Create the hour hand
hour_hand = turtle.Turtle()
hour_hand.shape("arrow")
hour_hand.shapesize(1, 5)
hour_hand.penup()
hour_hand.goto(0, 0)

# Create the minute hand
minute_hand = turtle.Turtle()
minute_hand.shape("arrow")
minute_hand.shapesize(1, 8)
minute_hand.penup()
minute_hand.goto(0, 0)

# Create the second hand
second_hand = turtle.Turtle()
second_hand.shape("arrow")
second_hand.shapesize(1, 10)
second_hand.penup()
second_hand.goto(0, 0)

# Create the time display
time_display = turtle.Turtle()
time_display.hideturtle()
time_display.penup()
time_display.goto(0, 250)

# Function to update the clock hands and time display
def update_clock():
    now = datetime.datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second

    # Calculate the angles for the clock hands
    hour_angle = (hour * 360 / 12) + (minute * 360 / 12 / 60)
    minute_angle = (minute * 360 / 60)
    second_angle = (second * 360 / 60)

    # Update the clock hands
    hour_hand.setheading(-hour_angle + 90)
    minute_hand.setheading(-minute_angle + 90)
    second_hand.setheading(-second_angle + 90)

    # Update the time display
    time_string = f"{hour:02d}:{minute:02d}:{second:02d}"
    time_display.clear()
    time_display.write(time_string, align="center", font=("Arial", 24, "normal"))

    # Schedule the next update
    screen.ontimer(update_clock, 1000)

# Start updating the clock
update_clock()

# Keep the window open
turtle.done()
