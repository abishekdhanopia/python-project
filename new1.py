from PIL import Image
import turtle

# Load the image
img = Image.open("new.jpg")

# Convert to black and white
img_bw = img.convert("L")

# Create a Turtle screen
screen = turtle.Screen()
screen.setup(img.width, img.height)
screen.setworldcoordinates(0, img.height, img.width, 0)

# Create a Turtle object
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed (0 is the fastest)

# Function to draw the image
def draw_image():
    for y in range(img_bw.height):
        for x in range(img_bw.width):
            pixel_color = img_bw.getpixel((x, y))
            if pixel_color < 128:  # Black
                t.penup()
                t.goto(x, img_bw.height - y)
                t.pendown()
                t.dot()

# Draw the image
draw_image()

# Hide Turtle and display
t.hideturtle()
screen.mainloop()
