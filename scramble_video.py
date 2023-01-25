import os
import random
import cv2

# specify input folder
input_folder = "path/to/input/folder"

# create list of image file names
image_files = [f for f in os.listdir(input_folder) if f.endswith(".jpg") or f.endswith(".png")]

# specify output video file name
output_file = "output.avi"

# create video writer object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_file, fourcc, 30.0, (1920, 1080))

# loop through image files
for file_name in image_files:
    # read image
    image = cv2.imread(os.path.join(input_folder, file_name))

    # scramble image into smeared pixel pattern
    rows, cols, channels = image.shape
    for i in range(rows):
        for j in range(cols):
            smeared = random.randint(0, 10)
            if smeared == 0:
                image[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # write image to video
    out.write(image)

# release video writer object
out.release()
