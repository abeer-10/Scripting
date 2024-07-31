from PIL import Image, ImageFilter

img = Image.open('Scripting/Pokedex/pikachu.jpg')
print(img)

# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save('blur_pikachu.png', 'png')

# bw = img.convert('L')
# bw.save('bw_pikachu.png','png')
# bw.show()

# rotate=img.rotate(180)
# rotate.save('rotate_pikachu.png','png')
# rotate.show()

# resize_bw = bw.resize((350,350))
# resize_bw.save('resize_bw.png','png')
# resize_bw.show()

# img1=Image.open('Scripting/astro.jpg')
# print(img1.size)
# img1.thumbnail((400,400))                                          #Thumbnail function resizes the photo but keeps the aspect ratio same.
# img1.save('img1_compressed.jpeg','jpeg')

import sys
import os

image_folder = sys.argv[1]                                          # Grab first and second argument
output_folder = sys.argv[2]
print(image_folder,output_folder)
# if not os.path.exists(output_folder):                               # Check if folder exists, if not create one
#     os.makedirs(output_folder)

# for filename in os.listdir(image_folder):
#     img = Image.open(f'{image_folder}{filename}')
#     clean_name = os.path.splitext(filename)[0]                      # We use 'splitext' coz if we run code without this it will be like .jpg.png
#     print(clean_name)