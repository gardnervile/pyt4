from PIL import Image

image_rgb = Image.open("monro.jpg")
red, green, blue = image_rgb.split()

coordinates = (100, 0, red.width, red.height)
cropped_image = red.crop(coordinates) 
coordinates = (50, 0 ,red.width - 50, red.height)
middle_image = red.crop(coordinates) 
blended_image = Image.blend(cropped_image, middle_image, 0.5)

coordinates = (0, 0, blue.width - 100, blue.height)
right_blue = blue.crop(coordinates)
coordinates = (50, 0, blue.width - 50, blue.height)
mid_blue = blue.crop(coordinates)
blended_blue = Image.blend(right_blue, mid_blue, 0.5)

coordinates = (50, 0, green.width - 50, green.height)
cropped_green = green.crop(coordinates)

merged = Image.merge("RGB", (blended_image, cropped_green, blended_blue))

new_size = (80, 70)
avatar = merged.resize(new_size)
avatar.save("avatar.jpg")
