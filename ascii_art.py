from PIL import Image

# Open the image
image = Image.open("image.jpg")

# Convert the image to grayscale
gray_image = image.convert("L")

# Define the ASCII characters to use for the grayscale values
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ","]

# Resize the image to a smaller size (optional)
gray_image = gray_image.resize((80, 40))

# Get the pixel data from the image
pixels = gray_image.getdata()

# Create the ASCII art string
ascii_art = ""
for pixel in pixels:
    ascii_art += ASCII_CHARS[pixel // 25]

# Print the ASCII art
print(ascii_art)
