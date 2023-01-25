import numpy as np
from PIL import Image
import math

def scramble_pixels(image_file, output_file):
    # Open the image file
    img = Image.open(image_file)
    
    # Convert the image to a numpy array
    img_array = np.array(img)
    
    # Get the shape of the image array
    rows, cols, _ = img_array.shape
    
    # Create an empty array for the new image
    new_img_array = np.zeros_like(img_array)
    
    # Define the golden ratio
    golden_ratio = 1.618
    
    # Iterate over the pixels in the image array
    for i in range(rows):
        for j in range(cols):
            # Calculate the new position of the pixel using the golden ratio
            new_i = int(i*golden_ratio) % rows
            new_j = int(j*golden_ratio) % cols
            
            # Smear the pixel to the new position
            new_img_array[new_i, new_j] = img_array[i, j]
            
    # Convert the numpy array back to an image
    new_img = Image.fromarray(np.uint8(new_img_array))
    
    # Save the new image to the specified output file
    new_img.save(output_file)
