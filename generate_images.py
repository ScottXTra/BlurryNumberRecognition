import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# Create directories for each number class
for i in range(10):
    os.makedirs('data/train/' + str(i), exist_ok=True)
for i in range(10):
    os.makedirs('data/val/' + str(i), exist_ok=True)
for i in range(10):
    os.makedirs('data/test/' + str(i), exist_ok=True)
# Generate a random number of images for each class
num_images = 5000

for i in range(10):
    for j in range(num_images):
        # Create a blank image
        img = Image.new('L', (32, 32), color=255)
        draw = ImageDraw.Draw(img)

        # Draw the number on the image with random position, size and rotation
        size = np.random.randint(20, 27)
        font = ImageFont.truetype("arial.ttf", size)
        text_width, text_height = draw.textsize(str(i), font=font)
        position = (np.random.randint(0, 32 - text_width), np.random.randint(0, 32 - text_height))
        angle = np.random.randint(-45, 45)
        draw.text(position, str(i), fill='black', font=font, angle=angle)
        
        # Apply random noise to the image
        img_array = np.array(img)
        img_array = np.clip(img_array + np.random.normal(scale=20, size=img_array.shape), 0, 255)
        img = Image.fromarray(img_array.astype(np.uint8))
        
        # Apply a random blurring factor to the image
        blur_factor = np.random.randint(2, 3)
        img = img.filter(ImageFilter.GaussianBlur(blur_factor))
        
        # Save the image
        img.save(f"data/train/{i}/{i}_{j}.png")
num_images = 5000
for i in range(10):
    for j in range(num_images):
        # Create a blank image
        img = Image.new('L', (32, 32), color=255)
        draw = ImageDraw.Draw(img)

        # Draw the number on the image with random position, size and rotation
        size = np.random.randint(20, 27)
        font = ImageFont.truetype("arial.ttf", size)
        text_width, text_height = draw.textsize(str(i), font=font)
        position = (np.random.randint(0, 32 - text_width), np.random.randint(0, 32 - text_height))
        angle = np.random.randint(-45, 45)
        draw.text(position, str(i), fill='black', font=font, angle=angle)
        
        # Apply random noise to the image
        img_array = np.array(img)
        img_array = np.clip(img_array + np.random.normal(scale=20, size=img_array.shape), 0, 255)
        img = Image.fromarray(img_array.astype(np.uint8))
        
        # Apply a random blurring factor to the image
        blur_factor = np.random.randint(2, 3)
        img = img.filter(ImageFilter.GaussianBlur(blur_factor))
        
        # Save the image
        img.save(f"data/val/{i}/{i}_{j}.png")
num_images = 50
for i in range(10):
    for j in range(num_images):
        # Create a blank image
        img = Image.new('L', (32, 32), color=255)
        draw = ImageDraw.Draw(img)

        # Draw the number on the image with random position, size and rotation
        size = np.random.randint(20, 27)
        font = ImageFont.truetype("arial.ttf", size)
        text_width, text_height = draw.textsize(str(i), font=font)
        position = (np.random.randint(0, 32 - text_width), np.random.randint(0, 32 - text_height))
        angle = np.random.randint(-45, 45)
        draw.text(position, str(i), fill='black', font=font, angle=angle)
        
        # Apply random noise to the image
        img_array = np.array(img)
        img_array = np.clip(img_array + np.random.normal(scale=20, size=img_array.shape), 0, 255)
        img = Image.fromarray(img_array.astype(np.uint8))
        
        # Apply a random blurring factor to the image
        blur_factor = np.random.randint(2, 3)
        img = img.filter(ImageFilter.GaussianBlur(blur_factor))
        
        # Save the image
        img.save(f"data/test/{i}/{i}_{j}.png")