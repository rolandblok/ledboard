from PIL import Image
im = Image.open("regenboog.png")

import ledmatrix
m = ledmatrix.ledmatrix()
m.set_image(0, 0, im)
