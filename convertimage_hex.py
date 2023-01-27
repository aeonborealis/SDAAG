from PIL import Image
import io

# Open the image file
image = Image.open("image.png")

# Create a binary stream object from the image
image_binary = io.BytesIO()

# Save the image in PNG format to the binary stream
image.save(image_binary, format='PNG')

# Get the binary data from the stream
binary_data = image_binary.getvalue()

# Convert the binary data to a hexadecimal string
hex_data = binary_data.hex()

# Print the hexadecimal string
print(hex_data)
