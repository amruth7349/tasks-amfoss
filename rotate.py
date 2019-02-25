from PIL import Image
oswald = Image.open('oswald.png')
oswald.rotate(270).save('rotated.png')
image_file = Image.open("oswald.png")
image_file = image_file.convert('1')
image_file.save('oswald.png')
oswald = Image.open('oswald.png')
oswald.transpose(Image.FLIP_LEFT_RIGHT).save('oswald2.png')
