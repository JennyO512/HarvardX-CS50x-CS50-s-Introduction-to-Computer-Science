from PIL import Image, ImageOps, ImageFilter

before = Image.open("stadium.bmp")

after = ImageOps.reflect(before)
after.save("outgrey.bmp")
