import numpy as np
from PIL import Image
import random

def smear_pixels(image_file, output_file):
    # Open the image file
    img = Image.open(image_file)
    
    # Convert the image to a numpy array
    img_array = np.array(img)
    
    # Get the shape of the image array
    rows, cols, _ = img_array.shape
    
    # Iterate over the pixels in the image array
    for i in range(rows):
        for j in range(cols):
            # Choose a random pixel to smear the current pixel to
            smear_i = random.randint(0, rows-1)
            smear_j = random.randint(0, cols-1)
            
            # Smear the current pixel to the chosen pixel
            img_array[smear_i, smear_j] = img_array[i, j]
            
    # Convert the numpy array back to an image
    smeared_img = Image.fromarray(np.uint8(img_array))
    
    # Save the smeared image to the specified output file
    smeared_img.save(output_file)
# You can use the code like this:
# smear_pixels("input.jpg", "output.jpg"
