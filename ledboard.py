from PIL import Image
im = Image.open("regenboog.png")
im = im.resize((14,14))

import ledmatrix
m = ledmatrix.ledmatrix()

m.set_image(0, 0, im)
