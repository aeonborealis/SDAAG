from PIL import Image
from ascii_art import ascii_art

# Open the image
image = Image.open("frame.jpg")

# Convert the image to grayscale
gray_image = image.convert("L")

# Create an ASCII art version of the image
ascii_image = ascii_art(gray_image)

# Print the ASCII art image
print(ascii_image)
