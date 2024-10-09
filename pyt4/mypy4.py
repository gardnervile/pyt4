from PIL import Image

image_rgb = Image.open("monro.jpg")
red, greem, blue = image_rgb.split()

image = Image.open("red.jpg")
coordinates = (100, 0, image.width, image.height)
cropped_image = image.crop(coordinates) 

image = Image.open("red.jpg")
coordinates = (50,0 ,image.width - 50, image.height)
middle_image = image.crop(coordinates) 

image1 = Image.open("cropped_image.jpg")
image2 = Image.open("middle_image.jpg")
blended_image = Image.blend(image1, image2, 0.5)

image = Image.open("blue.jpg")
coordinates = (0, 0, image.width - 100, image.height)
right_blue = image.crop(coordinates)

image = Image.open("blue.jpg")
coordinates = (50, 0, image.width - 50, image.height)
mid_blue = image.crop(coordinates)

image1 = Image.open("right_blue.jpg")
image2 = Image.open("mid_blue.jpg")
blended_blue = Image.blend(image1, image2, 0.5)

image = Image.open("green.jpg")
coordinates = (50, 0, image.width - 50, image.height)
cropped_green = image.crop(coordinates)

r = Image.open("blended_image.jpg")
g = Image.open("cropped_green.jpg")
b = Image.open("blended_blue.jpg")
merged = Image.merge("RGB", (r, g, b))

image = Image.open("merged.jpg")
new_size = (80, 70)
avatar = image.resize(new_size)
avatar.save("avatar.jpg")
