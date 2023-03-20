from PIL import Image, ImageOps, ImageFilter

before = Image.open("stadium.bmp")

after = ImageOps.grayscale(before)
after.save("outgrey.bmp")
