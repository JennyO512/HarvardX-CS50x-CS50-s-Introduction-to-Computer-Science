from PIL import Image, ImageFilter

before = Image.open("stadium.bmp")
after = before.filter(ImageFilter.BoxBlur(1))
after.save("out4.bmp")
