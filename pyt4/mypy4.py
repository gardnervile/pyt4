from PIL import Image
image = Image.open("merged_final.jpg")
new_size = (80, 70)
avatar = image.resize(new_size)
avatar.save("avatar.jpg")