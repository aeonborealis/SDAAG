from PIL import Image, ImageDraw, ImageFont
import random

def warp_text(text:str)->None:
    # Create a blank image with a white background
    img = Image.new('RGB', (400, 400), color = (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Select a random font and size
    font = ImageFont.truetype("arial.ttf", 36)

    # Draw the text on the image
    d.text((10,10), text, font=font, fill=(0,0,0))

    # Apply random distortions to the text
    img = img.rotate(random.randint(-30, 30), resample=Image.BICUBIC)
    img = img.transform((400, 400), Image.AFFINE, (1, random.uniform(-0.3, 0.3), random.randint(-10, 10), 0, 1, random.randint(-10, 10)))
    img = img.filter(ImageFilter.BLUR)

    # Save the image
    img.save('warped_text.png')

warp_text("Hello World")
